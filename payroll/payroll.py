from employee.employee import Employee

class Payroll:
    def __init__(self, file_name):
        # self.employees = self.read_input_file(file_name)
        self.employees = []


    def _calculate_pay(self):
        """
        Calculates and prints the total amount to be paid to each employee based on their work schedule and hourly wage.

        Reads the employee data from the input file provided during initialization, and for each employee, calculates the total
        amount to be paid based on their work schedule and hourly wage. The results are printed to the console in the format
        "The amount to pay {employee name} is: {total pay} USD".

        Returns:
            None
        """
        
        #TODO: iterate by employees.
        employee = {"name": "RENE", "schedule": "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"}
        total_pay = 215
        print(f"The amount to pay {employee['name']} is: {total_pay} USD")

    def read_input_file(self, file_name):
        employees = []
        with open(file_name, "r") as f:
            #TODO: process input file
            pass
        return employees