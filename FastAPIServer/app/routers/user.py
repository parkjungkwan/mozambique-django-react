from fastapi import APIRouter
from app.repositories.user import find_users, find_users_legacy
router = APIRouter()

@router.get("/")
async def get_users():
    return {"data": find_users()}

