from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create the engine
engine = create_engine('sqlite:///db/db.sqlite')


# Create the base
Base = declarative_base()


# Create the session
Session = sessionmaker(bind=engine)
session = Session()


