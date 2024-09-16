from api.utils.database import sql_db
from sqlalchemy import Integer, String, ForeignKey, delete, select
from sqlalchemy.orm import mapped_column, Mapped
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from api.models.User import User

class Wishlist(sql_db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(Integer, ForeignKey('user.user_id'))
    course_code: Mapped[str] = mapped_column(String(50), ForeignKey('course.course_code'))
    # comments = DictField()

    def __repr__(self) -> str:
        return f"Wishlist(id={self.id}, username={self.username}, course_code={self.course_code}, course_name={self.course_name})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # def expand(self):
    #     ret = {
    #         "username": self.username,
    #         "course": self.course,
    #         "comments": self.comments,
    #     }
    #     return ret