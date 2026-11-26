#!/usr/bin/python3
"""Defines the City class for SQLAlchemy ORM."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store Cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id (sqlalchemy.Integer): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
