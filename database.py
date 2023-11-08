from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import get_settings

settings = get_settings()

DATABASE_URL = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_SERVER}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(DATABASE_URL)

sess = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()