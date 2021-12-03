#
#   FastAPI uses pydantic modedels ("schemas") to send or receive data
#   of a predefined format in the routers requests and responses
#
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# common attributes for both creating and displaying data
class SensorBase(BaseModel):
    owner_id: int
    data_time: datetime
    value: float


class SensorCreate(SensorBase):
    pass


# define that orm_mode = True so that pydantic can read data other than dictionaries
# (like ORM models returned by db.query()) so that you can declare the class
# in the response_model argument in your path operations
class Sensor(SensorBase):
    id: int
    owner_id = int

    class Config:
        orm_mode = True


class ShowSensor(SensorBase):
    owner_id = int
    value = float

    class Config:
        orm_mode = True


# common attributes for both creating and displaying data
class UserBase(BaseModel):
    email: str


# for creating a user
class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    sensors: List[SensorBase] = []

    class Config:
        orm_mode = True


class ShowUser(UserBase):
    username: Optional[str] = None

    class Config:
        orm_mode = True
