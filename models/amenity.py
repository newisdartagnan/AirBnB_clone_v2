#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,  String, ForeignKey
from os import getenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship("Place", secondary='place_amenity',
                                       back_populates="amenities")
if __name__ == "__main__":
    # ...
    # Définition des classes

    # Création des tables dans la base de données
    Base.metadata.create_all(engine)

