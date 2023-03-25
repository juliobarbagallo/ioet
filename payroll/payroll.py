from employee.employee import Employee

class Payroll:
    def __init__(self, file_name):
        self.rates = {
            "MO": [(0, 540, 25), (540, 1080, 15), (1080, 1440, 20)],
            "TU": [(0, 540, 25), (540, 1080, 15), (1080, 1440, 20)],
            "WE": [(0, 540, 25), (540, 1080, 15), (1080, 1440, 20)],
            "TH": [(0, 540, 25), (540, 1080, 15), (1080, 1440, 20)],
            "FR": [(0, 540, 25), (540, 1080, 15), (1080, 1440, 20)],
            "SA": [(0, 540, 30), (540, 1080, 20), (1080, 1440, 25)],
            "SU": [(0, 540, 30), (540, 1080, 20), (1080, 1440, 25)]
        }
        self.employees = self.read_input_file(file_name)

    def calculate_pay(self):
        for employee in self.employees:
            total_pay = 0
            for day in employee.schedule:
                for time in employee.schedule[day]:
                    start_time, end_time = time.split("-")
                    start_hour, start_minute = start_time.split(":")
                    end_hour, end_minute = end_time.split(":")
                    start_hour, start_minute, end_hour, end_minute = int(start_hour), int(start_minute), int(end_hour), int(end_minute)
                    start_minutes = start_hour * 60 + start_minute
                    end_minutes = end_hour * 60 + end_minute
                    for rate_start, rate_end, rate in self.rates[day]:
                        overlap_start = max(start_minutes, rate_start)
                        overlap_end = min(end_minutes, rate_end)
                        if overlap_start < overlap_end:
                            total_pay += (overlap_end - overlap_start) / 60 * rate
            employee.set_amount_to_earn(total_pay)

    def read_input_file(self, file_name):
        employees = []
        with open(file_name, "r") as f:
            for line in f.readlines():
                name, schedule_str = line.strip().split("=")
                schedule = {}
                for item in schedule_str.split(","):
                    day, time = item[:2], item[2:]
                    if day not in schedule:
                        schedule[day] = []
                    schedule[day].append(time)
                employees.append(Employee(name, schedule))
        return employees