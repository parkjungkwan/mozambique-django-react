from app.database import engine, conn
from app.models.user import User
import pymysql
from sqlalchemy.orm import sessionmaker
pymysql.install_as_MySQLdb()

def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(User).all()