from api.models.sqlModel.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy import String, delete, select, update
from sqlalchemy.orm import mapped_column, Mapped

class User(sql_db.Model):
    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    
    def to_json(self):
        return {"username": self.username}

    def __repr__(self) -> str:
        return f"User(username={self.username})"

    @classmethod
    def get(cls, username):
        stmt = (
            select(cls)
            .filter_by(username = username)
        )
        results = sql_db.session.execute(stmt).first()
        return results
        
    
    @classmethod
    def create(cls, username, password):
        usr = cls(username=username, password=password)
        sql_db.session.add(usr)
        sql_db.session.commit()
        return True

    @classmethod
    def delete(cls, username):
        stmt = (
            delete(cls)
            .where(cls.username == username)
            .execution_options(synchronize_session="fetch")
        )
        sql_db.session.execute(stmt)
        num_deleted = sql_db.session.commit()
        if num_deleted == 0:
          return False
        else:
            Wishlist.delete(username=username)
            return True
    
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

