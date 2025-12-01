import unittest
from loan_calculator import calculate_monthly_payment

class TestLoanCalculator(unittest.TestCase):
    def test_standard_case(self):
        # Principal: 10000, Rate: 5%, Years: 1
        # Expected: ~856.07
        payment = calculate_monthly_payment(10000, 5, 1)
        self.assertAlmostEqual(payment, 856.07, places=2)

    def test_zero_interest(self):
        # Principal: 100000, Rate: 0%, Years: 2
        # Expected: 100000 / 24 = 4166.666...
        payment = calculate_monthly_payment(100000, 0, 2)
        self.assertAlmostEqual(payment, 4166.67, places=2)

    def test_high_interest(self):
        # Principal: 1000, Rate: 100%, Years: 1
        # Monthly rate: 1/12. Num payments: 12
        payment = calculate_monthly_payment(1000, 100, 1)
        # Expected value calculation:
        # r = 1/12
        # n = 12
        # M = 1000 * ( (1/12) * (13/12)**12 ) / ( (13/12)**12 - 1 )
        # M approx 134.99...
        self.assertAlmostEqual(payment, 134.99, places=1)

if __name__ == '__main__':
    unittest.main()
