from fastapi_pagination import add_pagination

from app.utils.common.time import current_time

global API_TOKEN, router, app
import os
import sys
import logging
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.responses import HTMLResponse

from app.configs.env import DB_URL
from app.configs.database import init_db
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from app.routers.author.user import router as user_router
from app.routers.board.article import router as article_router
from app.routers.chatbot.foodbot import router as foodbot_router
from app.routers.chatbot.socket_demo import router as socket_router
from app.routers.common.page import router as page_router
from app.tests.author.user import router as test_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader


API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")
print(f" ################ app.main Started At {current_time()} ################# ")
router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(test_router, prefix="/test", tags=["test"])
router.include_router(socket_router, prefix="/chatbot", tags=["chatbot"])
router.include_router(foodbot_router, prefix="/foodbot", tags=["foodbot"])
router.include_router(page_router, prefix="/page", tags=["page"])
app = FastAPI()
add_pagination(app)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.get("/")
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div>
        <h1 style="width:400px;margin:50px auto">
            {current_time()} <br/>
            현재 서버 구동 중 입니다. 
         </h1>
    </div>
    </body>
        """)

@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/no-match-token")
async def no_match_token():
    return {"message": f"토큰 유효시간이 지났습니다."}

# handler = Mangum(app)