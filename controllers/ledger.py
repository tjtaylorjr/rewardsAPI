from flask import Blueprint, Response, jsonify, request
from operator import itemgetter
import json
from datetime import datetime
from utils import time_sort, spend_points, update_balance
import models as db

ledger = Blueprint('ledger', __name__, url_prefix='/api/v1')

# a function that returns the current point balances for each payer
@ledger.get('/account')
def get_balance():
    balance = db.balance

    return balance


# a function that accepts a json payload with transaction data and adds it to
# the service's data store.
@ledger.post('/account')
def post_transaction():
    trans = db.transactions
    bal = db.balance

    payload = request.get_json()
    payer, points = itemgetter(
        'payer', 'points')(payload)

    if points > 0:
        trans.append(payload)
        time_sort(trans)

        credit = {'payer': payer, 'points': points}
        update_balance([credit])

        return credit
    else:
        payout = abs(points)
        payr_lst = [item for item in trans if item['payer'] == payer]
        time_sort(payr_lst)

        if bal[payer] < payout:
            return Response(
                'Request rejected. Insufficient points to complete this transaction.', status=400
            )

        while payout > 0:
            funds = payr_lst[-1]
            data = spend_points(payout, funds)
            debit, d_payout, d_points = itemgetter(
                'debit', 'payout', 'points')(data)
            payout = d_payout
            if d_points == 0:
                payr_lst.pop()
            else:
                funds['points'] = d_points
                print(funds['points'])
                print(payr_lst[-1])
        update_balance([debit])
        return debit


#a function that posts redemption requests from the account holder.
@ledger.post('/account/rewards')
def post_redemption():
    records = db.transactions
    time_sort(records)

    payload = request.get_json()
    payout = payload['points']

    debits = []

    balance = db.balance
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

        update_balance(debits)
        return jsonify(debits)
    else:
        return Response(
            'Request rejected. Insufficient points to complete this transaction.',
            status=400
        )
