from datetime import datetime
from pydantic import BaseModel


class Article(BaseModel):
    art_seq : int
    title : str
    content : str
    create_at : datetime
    updated_at : datetime


    class Config:
        orm_mode = True