from payroll.payroll import Payroll
from utils.utils import calculate_payroll, add_employee, export_payroll_report

if __name__ == "__main__":
    payroll = Payroll("input.txt")
    options = {
        "1": lambda: calculate_payroll(payroll),
        "2": lambda: add_employee(payroll),
        "3": lambda: export_payroll_report(payroll),
        "4": lambda: exit()
    }
    while True:
        print("Options:")
        print("1) Generate payroll")
        print("2) Add employee")
        print("3) Export to file")
        print("4) Exit")
        choice = input("Enter your choice: ")
        try:
            options[choice]()
        except KeyError:
            print("Invalid choice")
