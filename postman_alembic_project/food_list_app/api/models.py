# this file contains code for data representation 
# we define "models" as SQLAlchemy Classes for our database structure

from sqlalchemy import Float, Column, Integer, String
from api.db import Base

class Food(Base):
    __tablename__ = "indo_food_list"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    cuisine = Column(String(10), nullable=False)
    google_rating = Column(Float, nullable=False)
    budget = Column(String(10), nullable=False)
    district_area = Column(String(10), nullable=False)
    # ... other columns

    def __repr__(self):
        return f"indo_food_list(id={self.id}, name='{self.name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cuisine": self.cuisine,
            "google_rating": self.google_rating,
            "budget": self.budget,
            "district_area": self.district_area,
            # ... add other relevant fields here
        }
  

class User(Base):
    __tablename__ = "user_list"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    country = Column(String, nullable=False)
    fav_restaurant = Column(String, nullable=False)
  # ... other columns

    def __repr__(self):
        return f"user_list(id={self.id}, name='{self.name}')"
  
