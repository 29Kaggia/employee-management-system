from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create a SQLite database and initialize tables
engine = create_engine('sqlite:///employee_management.db')
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

class Attendance(Base):
    __tablename__ = 'attendance'

    attendance_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)

class Payroll(Base):
    __tablename__ = 'payroll'

    payroll_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)

class Evaluation(Base):
    __tablename__ = 'evaluations'

    evaluation_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    rating = Column(Integer, nullable=False)

class AuditLog:
    def __init__(self, table_name, action, timestamp, user_id, details):
        self.table_name = table_name
        self.action = action
        self.timestamp = timestamp
        self.user_id = user_id
        self.details = details
# Create the tables in the database
Base.metadata.create_all(engine)

# Create an instance of the Employee model with data
new_employee = Employee(name='John Doe', position='Manager', salary=60000.0)

# Log the change in an audit table
audit_entry = AuditLog(
    table_name='employee',
    action='INSERT',
    timestamp=datetime.now(),
    user_id=1,  # Replace with the actual user ID
    details=f"New employee added: {new_employee.name}"
)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
