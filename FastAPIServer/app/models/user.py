from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

class User(Base):

    __tablename__="users"

    user_email = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    class Config:
        arbitrary_types_allowed = True