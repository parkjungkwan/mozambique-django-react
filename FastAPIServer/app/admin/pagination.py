from starlette.responses import JSONResponse
from faker import Faker
from app.database import get_db
from app.cruds.user import UserCrud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/page")
def pagination(db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 0
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t = page_cnt // page_size
    block_size = 0
    t2 = page_cnt % block_size
    block_cnt = t if (t2 == 0) else t + 1
    page_now = 0
    row_start = (page_now -1) * page_size
    t = page_now * page_size
    row_end = t-1 if t else 0
    page_start = 0
    page_end = 0

    block_now = 0

    print(f" count is {row_cnt}")
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=row_cnt))

def insert_many(db: Session = Depends(get_db)):
    s = Session()

    """
    
    ls = []
    
    objects = [
        User(name="u1"),
        User(name="u2"),
        User(name="u3")
    ]
    s.bulk_save_objects(objects)"""


