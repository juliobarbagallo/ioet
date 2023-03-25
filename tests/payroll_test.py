import unittest
from payroll.payroll import Payroll

class TestPayroll(unittest.TestCase):
    def test_read_input_file(self):
        payroll = Payroll("input.txt")
        employees = payroll.read_input_file("input.txt")
        self.assertEqual(len(employees), 3)

        rene = employees[0]
        self.assertEqual(rene.name, "RENE")
        self.assertEqual(rene.schedule["MO"], ["10:00-12:00"])
        self.assertEqual(rene.schedule["TU"], ["10:00-12:00"])
        self.assertEqual(rene.schedule["TH"], ["01:00-03:00"])
        self.assertEqual(rene.schedule["SA"], ["14:00-18:00"])
        self.assertEqual(rene.schedule["SU"], ["20:00-21:00"])

        astrid = employees[1]
        self.assertEqual(astrid.name, "ASTRID")
        self.assertEqual(astrid.schedule["MO"], ["10:00-12:00"])
        self.assertEqual(astrid.schedule["TH"], ["12:00-14:00"])
        self.assertEqual(astrid.schedule["SU"], ["20:00-21:00"])

        tito = employees[2]
        self.assertEqual(tito.name, "TITO")
        self.assertEqual(tito.schedule["MO"], ["09:00-12:00"])
        self.assertEqual(tito.schedule["WE"], ["10:00-12:00"])


    def test_file_not_found(self):
        file = "non_existing.txt"
        payroll = Payroll(file)
        self.assertEqual(payroll.read_input_file(file), [])

if __name__ == "__main__":
    unittest.main()