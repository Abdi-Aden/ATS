from lib2to3.pgen2 import driver
from turtle import distance
from pydantic import BaseModel, HttpUrl

#schema for the company
class Company(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    email: str


#schema for the executive
class Executive(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    email: str
    company_id: int
    company: Company


#schema for the branch
class Branch(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    email: str
    manager_id: int
    manager: Employee
    manager_name: str
    company_id: int
    company: Company


#schema for the department
class Department(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    email: str
    manager_id: int
    manager: Employee
    manager_name: str
    branch_id: int
    branch: Branch
    branch_name: str
    company_id: int
    company: Company


#schema for the employee
class Employee(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    department_id: int
    department: Department
    department_name: str
    branch_id: int
    branch: Branch
    branch_name: str
    company_id: int
    company: Company


# schema for vehicle
class Vehicle(BaseModel):
    id: int
    name: str
    model: str
    year: int
    company_id: int
    company: Company
    branch_id: int
    branch: Branch
    branch_name: str
    department_id: int
    department: Department
    department_name: str
    employee_id: int
    employee: Employee
    employee_name: str


# schema for trips with appoinments, origin, destination, start_date, end_date, driver, vehicle, signature, status
class Trip(BaseModel):
    id: int
    origin: str
    destination: str
    start_date: str
    end_date: str
    driver: Employee
    driver_id: int
    vehicle: Vehicle
    vehicle_id: int
    signature: str
    status: str
    employee_id: int
    employee: Employee


#schema for the login   
class Login(BaseModel):
    email: str
    password: str   

    
#schema for registration table with is, name, email, phone, address, employee_id
class Registration(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    employee_id: int
    employee: Employee




