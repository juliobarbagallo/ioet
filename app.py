from payroll.payroll import Payroll

if __name__ == "__main__":
    payroll = Payroll("input.txt")
    payroll._calculate_pay()
