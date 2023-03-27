[![Python application](https://github.com/juliobarbagallo/ioet/actions/workflows/python-app.yml/badge.svg)](https://github.com/juliobarbagallo/ioet/actions/workflows/python-app.yml)

# Employee Payment Calculator

This project is a simple employee payment calculator that takes a list of employees and their work hours as input, and calculates the amount to pay each employee based on their work schedule.

## Getting Started

To use this calculator, simply provide a text file called input.txt containing the work schedules for each employee, in the following format:
[Employee Name]=[Work Schedule]

1_ Create a new directory at your workdirectory and cd into it.

```bash
mkdir ioet
cd ioet
```

2_ Clone project to the new created directory and change to the new created directory.

```bash
git clone https://github.com/juliobarbagallo/ioet.git
cd ioet
```

## Usage

```bash
python app.py
```

## Tests

```bash
python tests/payroll_test.py
```

## Description

The first approach in order to solve the exercise was to see how I can handle the working time frames. So I came in with the tuple structure and thinking in minutes, so I made the class Rates at rates/rates.py, so each day has a list of tuples, where those tuples have the start, the end of the work times and the rate for that range. So then we can iterate for it and sum it.So once we have that, the start point was to read and process the input.txt file, with the data to be processed. The Payroll class handles this with the read_input_file, which opens the input.txt file, and iterates the file's lines and splits them to get the employee name and the schedule, so we can have an array, employees of objects Employees.
Then all the calculations happen at Payroll.calculate_pay(), which iterates the employees array and for each employee on the array sets the amount to earn using the setter Employee.set_amount_to_earn(). That is pretty much the logict.
Regarding the structure, it's all OOP, delegating the core of it to Employee and Payroll classes and everything handled by app.py.The tests were done using unittest and everything was splitted in packages in different directories.

