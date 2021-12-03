from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a sqlite database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create a SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal CLASS. Each instance of said class will be a separate database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class. Later we will inherit from this class to create each of the database models or classes
Base = declarative_base()

