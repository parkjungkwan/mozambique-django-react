from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return [{"user_email":"test1","passowrd":"1"},{"user_email":"test2","passowrd":"1"}
            ,{"user_email":"test3","passowrd":"1"}]