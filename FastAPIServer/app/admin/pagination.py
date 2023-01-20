from starlette.responses import JSONResponse
from faker import Faker
from app.database import get_db
from app.cruds.user import UserCrud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/page/{page}")
def pagination(page: int, db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 5
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t3 = page_cnt // page_size
    block_size = 5
    t4 = page_cnt % block_size
    block_cnt = t3 if (t4 == 0) else t3 + 1
    page_now = page
    row_start = page_size * (page_now - 1)
    block_now = page_now // block_size
    row_end = row_start + (page_size - 1) if page_now != page_cnt else row_cnt - 1
    page_start = block_now * block_size
    page_end = page_start + (block_size -1 ) if block_now != (block_cnt - 1) else page_cnt

    print("### 테스트 ### ")
    print(f"row_start ={row_start}")
    print(f"row_end ={row_end}")
    print(f"page_start ={page_start}")
    print(f"page_end ={page_end}")


    '''
    row_cnt = 11, page_size = 5
    page  row_start row_end
    1 = 0 ~ 4
    2 = 5 ~ 9
    3 = 10
    
     | ### 테스트 ###
    api   | row_start =5
    api   | row_end =10 -> 9
    api   | page_start =0
    api   | page_end =2
    api   |  count is 11

    '''
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


