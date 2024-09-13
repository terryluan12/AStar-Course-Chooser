from mongoengine import Document, StringField
from api.models.mongoModel.Wishlist import Wishlist

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    @classmethod
    def create(cls, username_, password_):
        usr = cls.objects(username=username_)
        Wishlist.create(username_)
        usr.update_one(set__username=username_, 
                       set__password=password_,
                       upsert=True)
        return True

    @classmethod
    def delete(cls, username_):
        usr = cls.objects(username=username_).get()
        if usr:
            usr.delete()
            wl = Wishlist.objects(username=username_).get()
            if wl:
                wl.delete()
            return True
        return False

    @classmethod
    def verify_password(cls, username_, password_):
        usr = cls.objects(username=username_).get()
        if usr and usr.password == password_:
                return True
        return False
    
    @classmethod
    def get_wishlist(cls, username_):
        return Wishlist.objects(username=username_).get()

    @classmethod
    def add_comment(cls, username_, code_, comment_):
        usr = cls.objects(username=username_).get()
        if usr:
            usr.comments[code_] = comment_
            usr.save()
            return True
        return False

