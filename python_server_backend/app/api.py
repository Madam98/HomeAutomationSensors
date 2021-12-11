from fastapi import FastAPI, Depends
from .routers import sensor_data, users, background
from .sql_app import models
from .sql_app.database import engine
from . import constants
from os import system


# make sure the database is created by running the db setup script
system(constants.__ROOT__ + "\\sqlite_db\\database_setup.py")

# global dependencies:
# app = FastAPI(dependencies=[Depends(get_query_token())])
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(sensor_data.router)
app.include_router(sensor_data.router)
app.include_router(background.router)