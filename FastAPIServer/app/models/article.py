from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker
from app.database import Base
from sqlalchemy_utils import UUIDType

class Article(Base):

    __tablename__ = 'articles'

    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)


    user = relationship('User', back_populates='articles')


    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True