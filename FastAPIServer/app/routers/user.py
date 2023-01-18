from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
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
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=message))

@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).login_user(request_user=dto)))

@router.get("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_user_by_token(request_user=dto)))

@router.put("/modify")
async def modify_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).update_user(id,dto,db)))

@router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).delete_user(id,dto,db)))

@router.get("/page/{page}")
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_users(page,db)))


@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_users_by_job(search, page,db)

