from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, DB_URL
import pymysql

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)

