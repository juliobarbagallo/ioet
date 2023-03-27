def calculate_payroll(payroll):
    payroll.calculate_pay()
    for employee in payroll.employees:
        print(f"The amount to pay to {employee.name} is: {employee.get_amount_to_earn()} USD")


def add_employee(payroll):
    name = input("Enter the employee name: ")
    schedule_str = input("Enter the employee schedule (format: MO09:00-17:00,TU09:00-17:00,...): ")
    with open("input.txt", "a") as f:
        f.write(f"\n{name}={schedule_str}")
    print(f"Employee {name} added to input file")
    payroll.employees = payroll.read_input_file("input.txt")


def export_payroll_report(payroll):
    payroll.calculate_pay()
    output_file_name = input("Enter the output file name: ")
    with open(output_file_name, "w") as f:
        for employee in payroll.employees:
            f.write(f"The amount to pay to {employee.name} is: {employee.get_amount_to_earn()} USD\n")
    print(f"Payroll exported to file {output_file_name}")
