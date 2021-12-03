from fastapi import Depends, Response, status, HTTPException, APIRouter
from ..sql_app import models, schemas
from ..sql_app.database import engine
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db


# initialize API router with all the common traits
router = APIRouter(
    prefix="/sensor-data",
    tags=["sensor data"],
    # dependencies=[Depends(get_token_header)],
    # dependencies=[Depends(get_db)],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

# add sensor


# show all current sensor values
@router.get("/", response_model=List[schemas.ShowSensor])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.Sensor).all()







