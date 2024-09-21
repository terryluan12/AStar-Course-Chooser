from typing import List
from api.models.Wishlist import Wishlist
from api.models.Session import Session
from api.utils.database import sql_db
from sqlalchemy import Integer, String, delete, select, update
from sqlalchemy.orm import relationship, mapped_column, Mapped
from flask import current_app
import time
import uuid
import jwt

class User(sql_db.Model):
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    wished_courses: Mapped[List["Course"]] = relationship(secondary=Wishlist.__table__, back_populates='subscribed_users')
    sessions: Mapped[List["Session"]] = relationship(back_populates='user')
    def to_json(self):
        return {"username": self.username}

    def __repr__(self) -> str:
        return f"User(username={self.username})"
    
    def getWishlist(self):
        return self.wished_courses if self.wished_courses else []
    
    def appendWishlist(self, course):
        if not course in self.wished_courses:
            self.wished_courses.append(course)
            sql_db.session.commit()
            return True
        return False

    def removeWishlist(self, course):
        if course in self.wished_courses:
            self.wished_courses.remove(course)
            sql_db.session.commit()
            return True
        return False

    def login(self):
        session_id = str(uuid.uuid4())
        token = jwt.encode({"username": self.username, "session_id": session_id, "created_time": str(time.time())}, current_app.config['SECRET_KEY'], algorithm="HS256")
        session = Session(session_id=session_id, user_id=self.user_id)
        self.sessions.append(session)
        sql_db.session.commit()
        return token


    @classmethod
    def get(cls, username):
        stmt = (
            select(cls)
            .filter_by(username = username)
        )
        results = sql_db.session.execute(stmt).scalar()
        return results
        
    
    @classmethod
    def put(cls, username, password):
        usr = cls(username=username, password=password)
        sql_db.session.add(usr)
        sql_db.session.commit()
        return True

    @classmethod
    def delete(cls, username, password):
        stmt = (
            delete(cls)
            .where(cls.username == username)
            .execution_options(synchronize_session="fetch")
        )
        sql_db.session.execute(stmt)
        sql_db.session.commit()
    
    @classmethod
    def update(cls, username, password):
        stmt = (
            update(cls)
            .where(cls.username == username)
            .values(password=password)
        )
        sql_db.session.execute(stmt)
        sql_db.session.commit()
        return True

    @classmethod
    def add_comment(cls, username, code, comment):
        usr = cls.objects(username=username).get()
        if usr:
            usr.comments[code] = comment
            usr.save()
            return True
        return False

