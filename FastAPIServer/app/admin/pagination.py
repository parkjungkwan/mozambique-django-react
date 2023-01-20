from starlette.responses import JSONResponse
from faker import Faker
from app.admin.utils import between_random_date
from app.database import get_db
from app.cruds.user import UserCrud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.user import UserDTO

router = APIRouter()

@router.get("/page/{request_page}")
def pagination(request_page: int, db: Session = Depends(get_db)):
    row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    response_page = request_page - 1  # 넘겨받은 page번호를 인덱스 값으로 전환
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t3 = page_cnt // page_size
    block_size = 10
    t4 = page_cnt % block_size
    block_cnt = t3 if (t4 == 0) else t3 + 1
    start_row_per_page = page_size * (response_page)
    response_block = (response_page) // block_size
    end_row_per_page = start_row_per_page + (page_size - 1) if request_page != page_cnt else row_cnt - 1
    start_page_per_block = response_block * block_size
    end_page_per_block = start_page_per_block + (block_size -1 ) if response_block != (block_cnt - 1) else page_cnt

    print("### 테스트 ### ")
    print(f"start_row_per_page ={start_row_per_page}")
    print(f"end_row_per_page ={end_row_per_page}")
    print(f"start_page_per_block ={start_page_per_block}")
    print(f"end_page_per_block ={end_page_per_block}")

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
@router.get("/many")
def insert_many(db: Session = Depends(get_db)):

    print(f" Faker 작동 ")
    [ UserCrud(db).add_user(create_faker_user()) for i in range(100)]

def create_faker_user():
    faker = Faker('ko_KR')
    return UserDTO(email=faker.email(),password="11aa",
                  username=faker.name(), birth=between_random_date(),
                  address=faker.city())
