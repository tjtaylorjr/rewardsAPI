

# a helper function that will tally all current points on the account for each
# payer
def count_points(list):
    totals = {}
    for item in list:
        if item['payer'] not in totals:
            totals[item['payer']] = item['points']
        else:
            totals[item['payer']] += item['points']
    return totals
