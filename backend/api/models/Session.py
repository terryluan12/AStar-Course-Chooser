from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import String, DateTime, Integer, ForeignKey, func
from api.utils.database import sql_db
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()


class Session(sql_db.Model):
    session_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.user_id"), unique=False)
    date_logged_in: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # user: Mapped["User"] = relationship(back_populates='sessions', cascade="all, delete-orphan", single_parent=True)
    user: Mapped["User"] = relationship(back_populates='sessions', single_parent=True)
    
    @classmethod
    def get(cls, session_id):
        return cls.query.filter_by(session_id=session_id).first()
    
    
    def logOut(self):
        sql_db.session.delete(self)
        # self.sessions.remove(session)
        sql_db.session.commit()