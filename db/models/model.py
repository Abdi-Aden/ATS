import datetime as _dt
import email
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database


# table for Company
class Company(_database.Base):
    __tablename__ = 'company'
    id = _sql.Column(_sql.Integer, primary_key=True)
    name = _sql.Column(_sql.String(50), nullable=False)
    address = _sql.Column(_sql.String(50), nullable=False)
    phone = _sql.Column(_sql.String(50), nullable=False)
    email = _sql.Column(_sql.String(50), nullable=False)
    logo = _sql.Column(_sql.String(50), nullable=False)
    slogan = _sql.Column(_sql.String(50), nullable=False)

# departments table with manager from employees table 
class Department(_database.Base):
    __tablename__ = 'departments'
    id = _sql.Column(_sql.Integer, primary_key=True)
    name = _sql.Column(_sql.String(50), nullable=False)
    phone = _sql.Column(_sql.String(50), nullable=False)
    address = _sql.Column(_sql.String(50), nullable=False)
    email = _sql.Column(_sql.String(50), nullable=False)
    manager_id = _sql.Column(_sql.Integer, _sql.ForeignKey('employees.id'))
    manager = _orm.relationship('Employee', backref='departments')
    manager_name = _sql.Column(_sql.String(50), nullable=False)
    

# employees table 
class Employee(_database.Base):
    __tablename__ = "employees"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(64), nullable=False, index=True)
    email = _sql.Column(_sql.String(64), unique=True, index=True)   
    phone = _sql.Column(_sql.String(64), index=True) 
    department_id = _sql.Column(_sql.Integer, _sql.ForeignKey("departments.id"), nullable=False)
    department = _orm.relationship("Department", back_populates="employees")
    position = _sql.Column(_sql.String(64), index=True)
    start_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, index=True)
    salary = _sql.Column(_sql.Float, nullable=False)
    is_supervisor = _sql.Column(_sql.Boolean, default=False, index=True)
    supervisor_id = _sql.Column(_sql.Integer, _sql.ForeignKey("employees.id"), index=True)
    supervisor = _orm.relationship("Employee", back_populates="subordinates")
    subordinates = _orm.relationship("Employee", back_populates="supervisor")


# vehicles with driver from employees table
class Vehicle(_database.Base):
    __tablename__ = "vehicles"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(64), nullable=False, index=True)
    make = _sql.Column(_sql.String(64), nullable=False, index=True)
    model = _sql.Column(_sql.String(64), nullable=False, index=True)
    year = _sql.Column(_sql.Integer, nullable=False, index=True)
    license_plate = _sql.Column(_sql.String(64), unique=True, index=True)
    driver_id = _sql.Column(_sql.Integer, _sql.ForeignKey("employees.id"), nullable=False)
    driver = _orm.relationship("Employee", back_populates="vehicles")
    capacity = _sql.Column(_sql.Integer, nullable=False)
    is_available = _sql.Column(_sql.Boolean, default=True, index=True)


# trips table with driver from employees table and vehicle from vehicles table
class Trip(_database.Base):
    __tablename__ = "trips"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    appointment_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, index=True)
    origin = _sql.Column(_sql.String(64), nullable=False, index=True)
    destination = _sql.Column(_sql.String(64), nullable=False, index=True)
    start_time = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, index=True)
    end_time = _sql.Column(_sql.DateTime, index=True)
    driver_id = _sql.Column(_sql.Integer, _sql.ForeignKey("employees.id"), nullable=False)
    driver = _orm.relationship("Employee", back_populates="trips")
    vehicle_id = _sql.Column(_sql.Integer, _sql.ForeignKey("vehicles.id"), nullable=False)
    vehicle = _orm.relationship("Vehicle", back_populates="trips")
    signature = _sql.Column(_sql.String(64), index=True)
    is_complete = _sql.Column(_sql.Boolean, default=False, index=True)


# registration table with is, name, email, phone, address, employee_id from employees table
class Registration(_database.Base):
    __tablename__ = "registration"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(64), nullable=False, index=True)
    email = _sql.Column(_sql.String(64), unique=True, index=True)   
    phone = _sql.Column(_sql.String(64), index=True) 
    address = _sql.Column(_sql.String(64), index=True)
    employee_id = _sql.Column(_sql.Integer, _sql.ForeignKey("employees.id"), nullable=False)
    employee = _orm.relationship("Employee", back_populates="registration")


#login table with email from employees table and password
class Login(_database.Base):
    __tablename__ = "logins"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String(64), unique=True, index=True,foreign_key="employees.email")
    password = _sql.Column(_sql.String(64), nullable=False)
    employee = _orm.relationship("Employee", back_populates="login")

