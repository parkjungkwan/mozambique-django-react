from abc import ABC
from typing import List

from app.admin.security import verify_password, generate_token
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO, UserUpdate
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        lastrowid = self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return lastrowid

    def login_user(self, request_user: UserDTO) -> User:
        userid = self.find_userid_by_email(request_user=request_user)
        if userid != "":
            request_user.userid = userid
            db_user = self.find_user_by_id(request_user)
            verified = verify_password(plain_password=request_user.password,
                                       hashed_password=db_user.password)
            if verified:
                new_token = generate_token(request_user.email)
                request_user.token = new_token
                self.update_token(db_user, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다"
        else:
            return "FAILURE: 이메일 주소가 존재하지 않습니다"

    def update_user(self, request_user: UserUpdate) -> str:
        db_user = self.find_user_by_id(request_user)
        for var, value in vars(request_user).items():
            setattr(db_user, var, value) if value else None
        is_success = self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        print(f" 수정완료 후 해당 ID : {is_success}")
        return is_success

    def update_token(self, db_user: User, new_token: str):
        is_success = self.db.query(User).filter(User.userid == db_user.userid)\
            .update({User.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_user)
        return is_success

    def update_password(self, request_user: UserDTO):
        user = User(**request_user.dict())
        is_success = self.db.query(User).filter(User.userid == user.userid) \
            .update({User.password: user.password}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(user)
        return is_success

    def delete_user(self, request_user: UserDTO) -> str:
        user = self.find_user_by_id(User.user_id)
        self.db.query(User).filter(User.userid == user.userid). \
            delete(synchronize_session=False)
        self.db.commit()
        user = self.find_user_by_id(User.user_id)
        return  "탈퇴 성공입니다." if user is None else "탈퇴 실패입니다."

    def find_all_users_per_page(self, page: int) -> List[User]:
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> UserDTO:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).one_or_none()

    def find_userid_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).one_or_none()
        if db_user is not None:
            return db_user.userid
        else:
            return ""

    def find_all_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()






