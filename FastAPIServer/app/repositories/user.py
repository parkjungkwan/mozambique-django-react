from sqlalchemy import select

from app.database import conn
from app.models.user import User
from app.schemas.user import UserDTO
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

def join(userDTO: UserDTO, db: Session)->str:
    user = User(**userDTO.dict())
    db.add(user)
    db.commit()
    return "success"

def exist_email(userDTO: UserDTO, db: Session):
    user = User(**userDTO.dict())
    db_user = db.query(user).filter(User.user_email == user.user_email).first()
    if db_user is not None:
        return True
    else:
        return False

def login(userDTO: UserDTO, db: Session):
    user = User(**userDTO.dict())
    print(f" email {user.user_email}")
    if exist_email(userDTO, db) == True:
        return db.query(user).filter(User.user_email==user.user_email,
                                    User.password==user.password).first()
    else:
        return "None-Email"

def update(id, item, db):
    return None

def delete(id, item, db):
    return None


def find_users(page:int, db: Session):
    print(f" page number is {page}")
    return db.query(User).all()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_user(id, db):
    return None

def find_users_by_job(search, page, db):
    return None