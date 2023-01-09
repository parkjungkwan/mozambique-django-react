from fastapi import APIRouter

from app.repositories.user import find_users

router = APIRouter()

@router.get("/")
async def get_users():
    print(" -- 1 -- ")
    # tp = pymysql_method()
    tp = find_users()
    print(" -- 2 -- ")
    return {"test": tp}

