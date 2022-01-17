from flask import Blueprint, Response, jsonify, request
import json
from datetime import datetime
from utils import count_points
import models as db

rewards = Blueprint('rewards', __name__, url_prefix='/api/v1')

# a function that returns the current point balances for each payer
@rewards.get('/account')
def get_balance():
    transactions = db.transactions
    balance = count_points(transactions)

    return balance
