from api.models.sqlModel.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy import String, delete, select
from sqlalchemy.orm import mapped_column, Mapped

class User(sql_db.Model):
    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    
    @classmethod
    def get(cls, username):
        stmt = (
            select(cls)
            .filter_by(username = username)
        )
        results = sql_db.session.execute(stmt).first()
        return results
        
    
    @classmethod
    def create(cls, username_, password_):
        usr = cls(username=username_, password=password_)
        sql_db.session.add(usr)
        sql_db.session.commit()
        return True

    @classmethod
    def delete(cls, username_, password):
        stmt = (
            delete(cls)
            .where(cls.username == username_)
            .where(cls.password==password)
            .execution_options(synchronize_session="fetch")
        )
        sql_db.session.execute(stmt)
        num_deleted = sql_db.session.commit()
        if num_deleted == 0:
          return False
        else:
            Wishlist.delete(username=username_)
            return True

    @classmethod
    def verify_password(cls, username_, password_):
        usr = sql_db.get_or_404(cls, username_)
        if usr.password == password_:
                return True
        return False
    
    @classmethod
    def get_wishlist(cls, username_):
        return Wishlist.get(username=username_)

    @classmethod
    def add_comment(cls, username_, code_, comment_):
        usr = cls.objects(username=username_).get()
        if usr:
            usr.comments[code_] = comment_
            usr.save()
            return True
        return False

