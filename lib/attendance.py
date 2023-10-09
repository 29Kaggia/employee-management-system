class Attendance:
    def __init__(self, attendance_id, employee_id, date, status):
        self.attendance_id = attendance_id
        self.employee_id = employee_id
        self.date = date
        self.status = status

    def __str__(self):
        return f"Attendance ID: {self.attendance_id}, Employee ID: {self.employee_id}, Date: {self.date}, Status: {self.status}"
