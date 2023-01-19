from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, paginate, add_pagination
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse
from app.cruds.user import UserCrud
from app.database import get_db
from app.schemas.user import UserDTO, UserUpdate, UserList

router = APIRouter()

@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).add_user(request_user=dto)))

@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).login_user(request_user=dto)))

@router.post("/logout", status_code=200)
async def logout_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).logout_user(request_user=dto)))

@router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.put("/modify")
async def modify_user(dto: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.put("/reset-password")
async def reset_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).reset_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).delete_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)

@router.get("/page/{page}",response_model=Page[UserList])
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    results = UserCrud(db).find_all_users_per_page(page)
    page_result = paginate(results)
    print(f"page_result : {page_result}")
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(page_result))


@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UserCrud(db).find_users_by_job(search, page)))

add_pagination(router)