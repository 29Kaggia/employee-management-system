class Evaluation:
    def __init__(self, evaluation_id, employee_id, date, rating):
        self.evaluation_id = evaluation_id
        self.employee_id = employee_id
        self.date = date
        self.rating = rating

    def __str__(self):
        return f"Evaluation ID: {self.evaluation_id}, Employee ID: {self.employee_id}, Date: {self.date}, Rating: {self.rating}"
