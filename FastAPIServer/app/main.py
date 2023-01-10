import os
import sys
import logging
from fastapi_sqlalchemy import DBSessionMiddleware
from .env import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE, DB_URL
from app.database import Base, engine, init_db

from .models.user import User

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter
from .routers.user import router as user_router
from datetime import datetime

print(f" ################ app.main Started At {datetime.now()} ################# ")



router = APIRouter()
router.include_router(user_router, prefix="/users",tags=["users"])
app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"message ": " Welcome Fastapi"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

