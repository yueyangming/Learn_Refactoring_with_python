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

    def volumeCreditsFor(aPerformance, play):
        result = 0
        # add volume credits
        result += max(aPerformance['audience'] - 30, 0)
        if play['type'] == 'comedy':
            result += math.floor(aPerformance['audience'] / 5)
        return result

    def usd(aNumber):
        result = '$%.2f' % (aNumber / 100)
        return result

    def totalVolumeCredits(invoice, plays):
        result = 0
        for perf in invoice['performances']:
            play = [x for x in plays.items() if x[1]['playID'] == perf['playID']][0][1]
            result += volumeCreditsFor(perf, play)
        return result

    totalAmount = 0
    result = 'Statement for {}'.format(invoice['customer'])

    for perf in invoice['performances']:
        play = [x for x in plays.items() if x[1]['playID'] == perf['playID']][0][1]

        # print line for this order
        result += '  {}: {}  ({} seats) \n'.format(play['name'], usd(amountFor(perf, play)), perf['audience'])
        totalAmount += amountFor(perf, play)

    result += 'Amount owed is {}\n'.format(usd(totalAmount))
    result += 'You earned {} credits\n'.format(totalVolumeCredits(invoice, plays))
    return result


if __name__ == '__main__':
    cwd = os.getcwd()
    invoices_json_path = os.path.join(cwd, 'invoices.json')
    plays_json_path = os.path.join(cwd, 'plays.json')

    invoices = load_json(invoices_json_path)
    plays = load_json(plays_json_path)

    result = statement(invoices, plays)
    print(result)
