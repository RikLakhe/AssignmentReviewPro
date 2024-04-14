from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from constants.db_config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# Replace with your actual database credentials
SQLALCHEMY_DATABASE_URL = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+":"+str(DB_PORT)+"/"+DB_NAME

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
