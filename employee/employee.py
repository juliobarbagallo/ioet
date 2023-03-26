class Employee:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.amount_to_earn = 0

    def set_amount_to_earn(self, amount):
        self.amount_to_earn = amount

    def get_amount_to_earn(self):
        return self.amount_to_earn
