from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.cruds.user import UserCrud
from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import current_time
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()

@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    userid = user_crud.find_userid_by_email(request_user=dto)
    if userid == "":
        dto.password = get_hashed_password(dto.password)
        user_crud.add_user(request_user=dto)
        message = "SUCCESS: 회원가입이 완료되었습니다"
    else:
        message = "FAILURE: 이메일이 이미 존재합니다"
    return JSONResponse(status_code=400, content=dict(msg=message))

@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    token_or_fail_message = user_crud.login_user(request_user=dto)
    return JSONResponse(status_code=200, content=dict(msg=token_or_fail_message))

@router.put("/modify/{id}")
async def modify_user(id:str, item: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.update_user(id,item,db)
    return {"data": "success"}

@router.delete("/delete/{id}", tags=['age'])
async def remove_user(id:str, item: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    message = user_crud.delete_user(id,item,db)
    return JSONResponse(status_code=400, content=dict(msg=message))

@router.get("/page/{page}")
async def get_users(page: int, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    ls = user_crud.find_users(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_user(id: str, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_user(id, db)
    return {"data": "success"}

@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_users_by_job(search, page,db)
    return {"data": "success"}

