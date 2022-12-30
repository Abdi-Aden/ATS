
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative

Base = _declarative.declarative_base()

engine = _sql.create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)    # Create tables
Session = _orm.sessionmaker(bind=engine)
session = Session()

# Path: Backend\main.py

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return
    
#create an employee class
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return


