from fastapi import FastAPI, Depends
from .routers import humidity_temperature, users, background
from .sql_app import models
from .sql_app.database import engine
from . import constants
from os import system


# make sure the database is created by running the db setup script
# run the database_setup script
system(constants.__ROOT__ + "\\sqlite_db\\database_setup.py")

# global dependencies:
# app = FastAPI(dependencies=[Depends(get_query_token())])
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# include all endpoint routers in the app instance
app.include_router(users.router)
app.include_router(humidity_temperature.router)
app.include_router(background.router)