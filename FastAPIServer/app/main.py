import os
import sys
from fastapi_sqlalchemy import DBSessionMiddleware

from .env import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from app.api.endpoints.url import Url
from fastapi import FastAPI, APIRouter
from app.models.user import User
from .routers.user import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}")
@app.get("/")
async def root():
    return {"message ": " Welcome FastApi"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

