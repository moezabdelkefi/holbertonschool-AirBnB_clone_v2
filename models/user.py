#!/usr/bin/python3
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user for the application"""
    
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    def __init__(self, *args, **kwargs):
        """Initializes a new user"""
        super().__init__(*args, **kwargs)
