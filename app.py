from payroll.payroll import Payroll

if __name__ == "__main__":
    payroll = Payroll("input.txt")
    while True:
        print("Options:")
        print("1) Generate payroll")
        print("2) Add employee")
        print("3) Export to file")
        print("4) Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            payroll.calculate_pay()
            for employee in payroll.employees:
                print(f"The amount to pay to {employee.name} is: {employee.get_amount_to_earn()} USD")
        elif choice == "2":
            name = input("Enter the employee name: ")
            schedule_str = input("Enter the employee schedule (format: MO09:00-17:00,TU09:00-17:00,...): ")
            with open("input.txt", "a") as f:
                f.write(f"\n{name}={schedule_str}")
            print(f"Employee {name} added to input file")
            payroll.employees = payroll.read_input_file("input.txt")
        elif choice == "3":
            payroll.calculate_pay()
            output_file_name = input("Enter the output file name: ")
            with open(output_file_name, "w") as f:
                for employee in payroll.employees:
                    f.write(f"The amount to pay to {employee.name} is: {employee.get_amount_to_earn()} USD\n")
            print(f"Payroll exported to file {output_file_name}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
