# define database models using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database connection details (replace with your credentials)
DATABASE_URL = "postgresql://postgres:6871@localhost:5432/dvdrental"

# Create SQLAlchemy engine
# this connection pool manages comms between python app and the DB, postgreSQL
engine = create_engine(DATABASE_URL)

# Create declarative base CLASS for models

Base = declarative_base()

# Define BlogPost model, that INHERITS from Base.
# when a class inherits from Base, SQLAlch handles mapping py objs to DB tables
# creating tables based on class attributes
# defining relationsips between models
# mapping dataypes to db col datatypes
class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

# Create database tables (if they don't exist)
# SQLAlch creates DB tables based on the structure of model classes. 
Base.metadata.create_all(engine)

# Create session class for interacting with database
# sessions are crucial. for transactions (series of ops) and object lifecycles
# it is the bridge between your app and the connection pool (engine). see 3rd param
# it retrieves a connection from the pool and return when done. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
