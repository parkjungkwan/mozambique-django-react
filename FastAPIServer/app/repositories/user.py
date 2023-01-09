from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session

from app.database import DATABASE
from app.models.user import User

engine = create_engine(DATABASE, encoding="utf-8", echo=True)
def find_users(db: Session):
    print(f" 2 db :: {db}")
    a = db.query(User).all()
    print(f" 3 users :: {a}")
    return a

def select_users():
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement)
        for user in users:
            print(user)


def main():
    with engine.connect() as conn:
        result = conn.execute(text("select * from users"))
        print(result.all())

