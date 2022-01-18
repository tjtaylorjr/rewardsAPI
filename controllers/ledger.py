from flask import Blueprint, Response, jsonify, request
import json
from datetime import datetime
from utils import count_points, time_sort, spend_points
import models as db

ledger = Blueprint('ledger', __name__, url_prefix='/api/v1')

# a function that returns the current point balances for each payer
@ledger.get('/account')
def get_balance():
    transactions = db.transactions
    balance = count_points(transactions)

    return balance


# a function that accepts a json payload with transaction data and adds it to
# the service's data store.
@ledger.post('/account')
def post_transaction():
    records = db.transactions

    payload = request.get_json()
    if payload['points'] > 0:
        records.append(payload)
        time_sort(records)

        return {'payer': payload['payer'], 'points': payload['points']}
    else:
        payout = abs(payload['points'])
        payer = payload['payer']

        payer_lst = [item for item in records if item['payer'] == payer]
        time_sort(payer_lst)

        balance = count_points(payer_lst)
        if sum(balance.values()) < payout:
            return Response(
                'Request rejected. Insufficient points to complete this transaction.', status=400
            )

        while payout > 0:
            funds = payer_lst[0]
            data = spend_points(payout, funds)
            payout = data['payout']
            if data['points'] == 0:
                payer_lst.pop(0)
            else:
                funds['points'] = data['points']

        return data['debit']


#a function that posts redemption requests from the account holder.
@ledger.post('/account/rewards')
def post_redemption():
    records = db.transactions
    time_sort(records)

    payload = request.get_json()
    payout = payload['points']

    debits = []
    balance = count_points(records)

    total_funds = sum(balance.values())
    if total_funds >= payout:
        while payout > 0:
            funds = records[0]
            data = spend_points(payout, funds)

            payout = data['payout']
            points = data['points']

            if points == 0:
                records.pop(0)

            else:
                records[0]['points'] = points

            debits.append(data['debit'])

        return jsonify(debits)
    else:
        return Response(
            'Request rejected. Insufficient points to complete this transaction.',
            status=400
        )
