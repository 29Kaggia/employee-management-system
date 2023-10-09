class Payroll:
    def __init__(self, payroll_id, employee_id, month, year, amount):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.month = month
        self.year = year
        self.amount = amount

    def __str__(self):
        return f"Payroll ID: {self.payroll_id}, Employee ID: {self.employee_id}, Month: {self.month}, Year: {self.year}, Amount: {self.amount}"
