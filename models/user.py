#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv


Storage = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Attributes:
        __tablename__ (str): Represents the table name, "users".
        email (Column): Represents a column containing a
            string (128 characters), can't be null.
        password (Column): Represents a column containing a
            string (128 characters), can't be null.
        first_name (Column): Represents a column containing a
            string (128 characters), can be null.
        last_name (Column): Represents a column containing a
            string (128 characters), can be null.
        places (relationship): Relationship with the "Place" class,
            with a back reference to "user" and cascade "delete".
    """
    __tablename__ = "users"
    if Storage = "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
                "Place",
                backref="user",
                cascade="all, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
