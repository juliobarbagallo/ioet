from payroll.payroll import Payroll

if __name__ == "__main__":
    payroll = Payroll("input.txt")
    payroll.calculate_pay()
    for employee in payroll.employees:
        print(f"The amount to pay {employee.name} is: {employee.get_amount_to_earn()} USD")

