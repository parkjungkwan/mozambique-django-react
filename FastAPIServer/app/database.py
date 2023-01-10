from typing import Generator
from .models.article import Article
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, DB_URL
import pymysql

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
SessionLocal = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)
Base.query = SessionLocal.query_property()

from models.user import User
async def init_db():
    print("-- Initialized the db 1 --")
    Base.metadata.create_all(bind=engine)
    SessionLocal.add(
        User(user_email="hong@test.com", user_name="홍길동", password="1"),
        User(user_email="you@test.com", user_name="유관순", password="1"),
        Article(title="테스트", content="글쓴 내용", user_id=None),
        Article(title="테스트2", content="글쓴 내용2", user_id=None)
    )
    SessionLocal.commit()

    print("-- Initialized the db 2 --")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

