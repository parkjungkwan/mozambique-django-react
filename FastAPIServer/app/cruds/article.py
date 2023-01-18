from abc import ABC
from typing import List
import pymysql
from sqlalchemy.orm import Session

from app.bases.article import ArticleBase
from app.models.article import Article
from app.schemas.article import ArticleDTO

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        self.db.add(article)
        self.db.commit()
        return "success"

    def update_article(self, request_article: ArticleDTO) -> str:
        pass

    def delete_article(self, request_article: ArticleDTO) -> str:
        self.find_article_by_seq(Article.seq)
        self.db.query(Article).delete()

    def find_all_articles(self, page: int) -> List[ArticleDTO]:
        return self.db.query(Article).all()

    def find_articles_by_userid(self, userid: str) -> ArticleDTO:
        pass

    def find_articles_by_title(self, title: str) -> List[ArticleDTO]:
        pass

    def find_article_by_seq(self, request_article: ArticleDTO) -> ArticleDTO:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.seq == article.seq).first()