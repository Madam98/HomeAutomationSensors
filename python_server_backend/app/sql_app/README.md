## /sql_app

The sql_app package consists of different modules used for interacting with the sqlite3 database using the SQLAlchemy framework.

- **database.py:** base sqlalchemy objects used to connect to the database and operate in SQLAlchemy.  
- **models.py:** a set of SQLAlchemy models mapping the sql database tables
- **schemas.py:** a set of pydantic models (also called schemas for differentiation's sake) used to establish the format of the HTTP request and response data.