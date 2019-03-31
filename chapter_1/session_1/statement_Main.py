# Arthor = Harold Yue
# Date = 2019.3.25

import os
import math

from utils import load_json


def statement(invoice, plays):
    def amountFor(perf, play):
        thisAmount = 0

        # As there is no switch in python, i use if statement instead.
        if play['type'] == 'tragedy':
            thisAmount = 40000
            if perf['audience'] > 30:
                thisAmount += 1000 * (perf['audience'] - 30)
            # break

        elif play['type'] == 'comedy':
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']
            # break

        else:
            raise UserWarning('unknown type: {}'.format(play['type']))
        return thisAmount

    totalAmount = 0
    volumeCredits = 0
    result = 'Statement for {}'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = [x for x in plays.items() if x[1]['playID'] == perf['playID']][0][1]

        thisAmount = amountFor(perf, play)

        # add volume credits
        volumeCredits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if play['type'] == 'comedy':
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += '  {}: $%.2f  ({} seats) \n'.format(play['name'], perf['audience']) %(thisAmount / 100)
        totalAmount += thisAmount
    result += 'Amount owed is $%.2f\n' % (totalAmount / 100)
    result += 'You earned $%.2f credits\n' % volumeCredits
    return result


if __name__ == '__main__':
    cwd = os.getcwd()
    invoices_json_path = os.path.join(cwd, 'invoices.json')
    plays_json_path = os.path.join(cwd, 'plays.json')

    invoices = load_json(invoices_json_path)
    plays = load_json(plays_json_path)

    result = statement(invoices, plays)
    print(result)
