from fastapi import Depends, Response, status, HTTPException, APIRouter
from ..sql_app import models
from ..sql_app.schemas import hum_temp_sensor
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from ..dependencies import get_db

# initialize API router with all the common traits
router = APIRouter(
    prefix="/hum-temp",
    tags=["humidity & temperature sensor"],
    # dependencies=[Depends(get_token_header)],
    # dependencies=[Depends(get_db)],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


# add a humidity & temperature record (for testing purposes)
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_new_record(request: hum_temp_sensor.HumTempAdd, db: Session = Depends(get_db)):
    new_record = models.HumidityTemperatureSensor(
        date_time=request.date_time,
        humidity=request.humidity,
        temperature=request.temperature)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"New added user": new_record}


# show all humidity & temperature values
@router.get("/", response_model=List[hum_temp_sensor.ShowHumTemp])
def get_records(limit: Optional[int] = None, db: Session = Depends(get_db)):
    hum_temp_model = models.HumidityTemperatureSensor
    query_res = db.query(hum_temp_model)
    res_len = query_res.count()
    if limit:
        return query_res.order_by(hum_temp_model.date_time).offset(res_len-limit).limit(limit).all()
    else:
        return query_res.order_by(hum_temp_model.date_time).all()









