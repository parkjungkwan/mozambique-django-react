from fastapi import APIRouter, Depends
from app.cruds.board.article import ArticleCrud
from sqlalchemy.orm import Session
from app.schemas.board.article import ArticleDTO
from app.configs.database import get_db

router = APIRouter()