from typing import List

from fastapi import APIRouter, Depends
from app.repositories.user import find_users
from sqlalchemy.orm import Session
from app.schemas.user import UserList
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[UserList])
async def get_users(db: Session = Depends(get_db)):
    print(f" 1 db :: {db}")
    return find_users(db=db)