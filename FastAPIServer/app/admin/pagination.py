from starlette.responses import JSONResponse

from app.database import get_db
from app.cruds.user import UserCrud
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/page")
def pagination(db: Session = Depends(get_db)):
    count = UserCrud(db).count_all_users()
    print(f" count is {count}")
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=count))


