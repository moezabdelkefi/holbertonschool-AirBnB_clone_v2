#!/usr/bin/python3
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(Base, BaseModel):
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        'Place', cascade="all, delete-orphan", backref='user')
    reviews = relationship(
        'Review', cascade="all, delete-orphan", backref='user')
