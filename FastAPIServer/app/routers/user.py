from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.user as dao
from app.database import get_db
from app.models.user import User

router = APIRouter()

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    return {"data": dao.find_users(db=db)}

@router.post("/login")
async def login(db: Session = Depends(get_db)):
    return {"data": dao.find_users(db=db)}

@router.post("/signup")
async def add(user: User):
    user_dict = user.dict()
    print(f"SignUp Inform : {user_dict}")





