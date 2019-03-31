# Arthor = Harold Yue
# Date = 2019.3.25

import os
import math

from utils import load_json


def statement(invoice, plays):
    def amountFor(aPerformance, play):
        result = 0

        # As there is no switch in python, i use if statement instead.
        if play['type'] == 'tragedy':
            result = 40000
            if aPerformance['audience'] > 30:
                result += 1000 * (aPerformance['audience'] - 30)
            # break

        elif play['type'] == 'comedy':
            result = 30000
            if aPerformance['audience'] > 20:
                result += 10000 + 500 * (aPerformance['audience'] - 20)
            result += 300 * aPerformance['audience']
            # break

        else:
            raise UserWarning('unknown type: {}'.format(play['type']))
        return result

    totalAmount = 0
    volumeCredits = 0
    result = 'Statement for {}'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = [x for x in plays.items() if x[1]['playID'] == perf['playID']][0][1]

        # add volume credits
        volumeCredits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if play['type'] == 'comedy':
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += '  {}: $%.2f  ({} seats) \n'.format(play['name'], perf['audience']) % (amountFor(perf, play) / 100)
        totalAmount += amountFor(perf, play)
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
