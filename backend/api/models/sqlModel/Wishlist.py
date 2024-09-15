from api.utils.database import sql_db
from sqlalchemy import Integer, String, delete, select
from sqlalchemy.orm import mapped_column, Mapped


class Wishlist(sql_db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    course_code: Mapped[str] = mapped_column(String(8), nullable=False)
    course_name: Mapped[str] = mapped_column(String(50), nullable=False)
    # comments = DictField()

    def __repr__(self) -> str:
        return f"Wishlist(id={self.id}, username={self.username}, course_code={self.course_code}, course_name={self.course_name})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def add_course(self, username, course_code, course_name):
        course = self(username=username, course_code=course_code, course_name=course_name)
        sql_db.session.add(course)
        sql_db.session.commit()

    @classmethod
    def remove_course(self, username, course_code):
        stmt = (
            delete(self)
            .where(self.username == username)
            .where(self.course_code == course_code)
            .execution_options(synchronize_session="fetch")
        )
        sql_db.session.execute(stmt)
        sql_db.session.commit()

    @classmethod
    def delete(self, username):
        stmt = (
            delete(self)
            .where(self.username == username)
            .execution_options(synchronize_session="fetch")
        )
        test = sql_db.session.execute(stmt)
        test2 = sql_db.session.commit()
        print(f'test1 is {test}, and test2 is {test2}')
    
    @classmethod
    def get(self, username):
        stmt = (
            select(self)
            .filter_by(username = username)
        )
        results = sql_db.session.execute(stmt).scalars().all()
        return results
        
    def expand(self):
        ret = {
            "username": self.username,
            "course": self.course,
            "comments": self.comments,
        }
        return ret