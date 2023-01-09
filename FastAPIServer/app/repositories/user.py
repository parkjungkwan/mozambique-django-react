import pymysql

from app.database import engine
from app.env import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
from app.models.user import User
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
pymysql.install_as_MySQLdb()
def find_users_legacy():
    conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
    cursor = conn.cursor()  # MySQL에 접속
    sql = "select * from users"  # 적용할 MySQL 명령어를 만들어서 sql 객체에 할당하면 됨
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(f"data: {data}")
    print(f"type is {type(result)}")
    # conn.close()  # 위에 작업한 내용 서버에 저장
    return result

def find_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(User).all()