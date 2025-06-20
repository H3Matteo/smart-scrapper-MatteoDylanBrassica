from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Musee(Base):
    __tablename__ = "musees"

    id = Column(String, primary_key=True)
    nom = Column(String)
    ville = Column(String)
    departement = Column(String)
    region = Column(String)
    theme = Column(String)
    annee = Column(Integer, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
