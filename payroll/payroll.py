from employee.employee import Employee
from rates.rates import Rates


class Payroll(Rates):
    MINUTES_PER_HOUR = 60
    
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
                total_pay += self._calculate_pay_by_day(day, employee.schedule[day])
            employee.set_amount_to_earn(total_pay)

    def _calculate_pay_by_day(self, day, times):
        total_pay = 0
        for time in times:
            start_time, end_time = time.split("-")
            start_minutes, end_minutes = self._get_minutes(start_time), self._get_minutes(end_time)
            for rate_start, rate_end, rate in getattr(self, day):
                overlap_start = max(start_minutes, rate_start)
                overlap_end = min(end_minutes, rate_end)
                if overlap_start < overlap_end:
                    total_pay += self._calculate_pay_by_time_period(overlap_start, overlap_end, rate)
        return total_pay

    def _calculate_pay_by_time_period(self, start_minutes, end_minutes, rate):
        return (end_minutes - start_minutes) / self.MINUTES_PER_HOUR * rate

    def _get_minutes(self, time):
        hour, minute = map(int, time.split(":"))
        return hour * self.MINUTES_PER_HOUR + minute

    def read_input_file(self, file_name):
        employees = []
        try:
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
        except FileNotFoundError:
            print(f"ERROR: File {file_name} not found")
            return []
        except ValueError as e:
            print(f"ERROR: {e}")
            return []
        return employees
