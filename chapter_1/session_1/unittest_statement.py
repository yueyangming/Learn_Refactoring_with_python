import unittest
import os

# path error
import sys
sys.path.append('/home/harold/PycharmProjects/Learn_Refactoring_with_python/chapter_1/session_1')

from utils import load_json
from statement_Main import statement


class UTest(unittest.TestCase):
    def setUp(self):
        cwd = '/home/harold/PycharmProjects/Learn_Refactoring_with_python/chapter_1/session_1'
        invoices_json_path = os.path.join(cwd, 'invoices.json')
        plays_json_path = os.path.join(cwd, 'plays.json')

        self.invoices = load_json(invoices_json_path)
        self.plays = load_json(plays_json_path)

    def test_statement_result(self):
        result = statement(self.invoices, self.plays)
        self.assertEqual(result, 'Statement for BigCo  Hamlet: $650.00  (55 seats) \n  As You Like It: $580.00  (35 seats) \n  Othello: $500.00  (40 seats) \nAmount owed is $1730.00\nYou earned 47 credits\n')

    def test_error_userwarning(self):
        pass


if __name__ == '__main__':
    unittest.main()
