from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE = f"mysql+pymysql://root:root@localhost:3306/mydb"
engine = create_engine(DATABASE, encoding="utf-8", echo=True)
SessionLacol = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = SessionLacol.query_property()


def get_db():
    try:
        db = SessionLacol()
        yield db
    finally:
        db.close()
import pymysql
import sys

