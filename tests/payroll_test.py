import unittest
from payroll.payroll import Payroll
from employee.employee import Employee

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


    def test_payroll_calculation(self):
        payroll = Payroll("input.txt")
        payroll.calculate_pay()

        assert payroll.employees[0].get_amount_to_earn() == 215.0
        assert payroll.employees[1].get_amount_to_earn() == 85.0
        assert payroll.employees[2].get_amount_to_earn() == 75.0

        self.assertEqual(payroll.employees[0].name, "RENE")
        self.assertEqual(payroll.employees[1].name, "ASTRID")
        self.assertEqual(payroll.employees[2].name, "TITO")

class TestEmployee(unittest.TestCase):
    def test_employee_class(self):
        employee = Employee("John", "MO10:00-12:00")
        assert employee.name == "John"
        assert employee.schedule == "MO10:00-12:00"
        assert employee.amount_to_earn == 0
        
        employee.set_amount_to_earn(100)
        assert employee.get_amount_to_earn() == 100


if __name__ == "__main__":
    unittest.main()