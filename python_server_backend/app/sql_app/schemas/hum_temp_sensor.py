#
#   FastAPI uses pydantic models ("schemas") to send or receive data of a predefined format
#
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# common attributes for both creating and displaying data
class HumTempBase(BaseModel):
    date_time: datetime
    humidity: float
    temperature: float


# a class used so that pydantic can read data other than simple python dictionaries
# (for example ORM models returned by db.query() - a sqlalchemy datatype)
# This allows to pass this class as a response_model argument in the API path operations
class HumidityTemperatureSensor(HumTempBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


class HumTempAdd(HumTempBase):
    # owner_id: int
    pass


class ShowHumTemp(HumTempBase):
    # owner_id: int

    class Config:
        orm_mode = True
