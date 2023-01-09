from app.database import engine, conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_users(db: Session):
    return db.query(User).all()