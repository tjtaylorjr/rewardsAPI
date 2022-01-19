from operator import itemgetter
import models as db


# a helper function to consume transaction points.  Provides logic to
# determine how points are spend and in what order.
def spend_points(payout, funds):
    payer = funds['payer']
    points = funds['points']

    # establish lowest value between payout and points
    lowest = points if points <= payout else payout

    # create a debit dict for post_payout function that represents a point
    # balance reduction, can be safely ignored by post_transaction route.
    debit = {'payer': payer, 'points': -lowest}

    # subtract the lowest variable value from both points and payout.  One
    # will end up zeroed out and the other will have the appropriate amount of
    # points deducted from it to complete the transaction.
    points -= lowest
    payout -= lowest

    #return debit dict along with new payout and points values
    return {'debit': debit, 'payout': payout, 'points': points}


# a simple helper function that sorts a list of dictionaries by the timestamp
# keys
def time_sort(lst):
    lst.sort(key=lambda item: item.get('timestamp'), reverse=True)
    return lst


# a helper function to pass data to the balance data store during transactions
def update_balance(trnxcs):
    bal = db.balance

    for trnxc in trnxcs:
        payer, points = itemgetter(
            'payer', 'points')(trnxc)

        if payer not in bal:
            bal[payer] = points
        else:
            bal[payer] += points

    return bal
