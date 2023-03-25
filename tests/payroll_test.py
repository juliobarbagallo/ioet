import unittest
from unittest.mock import patch
from io import StringIO
from payroll.payroll import Payroll

class PayrollTest(unittest.TestCase):
    def setUp(self):
        self.payroll = Payroll("input.txt")

    @patch('sys.stdout', new_callable=StringIO)
    def test_calculate_pay(self, mock_stdout):
        self.payroll._calculate_pay()
        expected_output = "The amount to pay RENE is: 215 USD\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()