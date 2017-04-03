import unittest
from Loan import loan_calculator

class LoanCalculator(unittest.TestCase):
    def test_accept_integers_values(self):
        self.assertEqual(loan_calculator(100000,12,12),112000)
