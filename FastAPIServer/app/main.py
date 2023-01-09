import os
import sys
from fastapi_sqlalchemy import DBSessionMiddleware

from .database import DATABASE

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from app.api.endpoints.url import Url
from fastapi import FastAPI, APIRouter
from app.models.user import User
from .routers.user import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DATABASE)
@app.get("/")
async def root():
    print(" -- 1 -- ")
    # tp = pymysql_method()
    tp = sqlalchemy_method()
    print(" -- 2 -- ")
    return {"message": tp}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

def pymysql_method():
    import pymysql

    HOSTNAME = 'host.docker.internal'
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = 'root'
    DATABASE = 'mydb'
    CHARSET = 'utf8'

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

def sqlalchemy_method():
    import pymysql
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+pymysql://root:root@host.docker.internal:3306/mydb", encoding="utf-8", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(User).all()
    print(f"type is {type(result)}")
    for row in result:
        print(f"data : {row}")
    return result