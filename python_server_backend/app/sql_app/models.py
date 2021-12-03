#
#   this is were all sqlalchemy ORM models (mapping the database tables) are defined
#
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)

    sensors = relationship("Sensor", back_populates="owner")


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
    value = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="sensors")

