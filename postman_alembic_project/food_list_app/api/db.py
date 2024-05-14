# this file contains code for database interaction and connection mgmt

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to your PostgreSQL database (replace placeholders)
engine = create_engine('postgresql://postgres:6871@localhost:5432/food_list')
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
