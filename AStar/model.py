# This is the model

from config import app, db

class Course(db.Document):
    code = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    syllabus = db.URLField()
    prereq = db.ListField()
    coreq = db.ListField()
    exclusion = db.ListField()
    keyword = db.ListField(required=True)

    @classmethod
    def get(cls, code_):
        return cls.objects(code=code_).get()
    
    @classmethod
    def get_requisite_graph(cls, code_):
        # TODO
        return


def val_course(stuff):
    return

class Wishlist(db.Document):
    username = db.StringField()
    course = db.ListField(db.ReferenceField(Course))

    @classmethod
    def create(cls,username_):
        usr = cls.objects(username=username_)
        usr.update_one(set__course=[],
                       upsert=True)
        return True

    @classmethod
    def add_course(self, code_):
        # code_ is a course object
        self.course.append(code_)
        self.save(validate=False)
    
    @classmethod
    def remove_course(self, code_):
        if code_ in self.course:
            self.course.remove(code_)
            self.save(validate=False)


class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    comments = db.DictField()
    wishlist = db.ReferenceField(Wishlist)

    @classmethod
    def create(cls, username_, password_):
        usr = cls.objects(username=username_)
        Wishlist.create(username_)
        wishlist_ = Wishlist.objects(username=username_).get()
        usr.update_one(set__username=username_, 
                       set__password=password_,
                       set__wishlist=wishlist_,
                       upsert=True)

        return True

    @classmethod
    def delete(cls, username_):
        usr = cls.objects(username=username_).get()
        if usr:
            usr.delete()
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


class Minor(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
    requisites = db.ListField(db.ListField(db.ListField)) 
            #[ (['code', 'code'], 2), (['code', 'code'], 1), ] 

    @classmethod
    def get(cls, name_):
        return cls.objects(name=name_).get()
    
    @classmethod
    def check(cls, codes_):
        ret = []

        for mn in cls.objects:
            print(f"checking {mn}")
            yes = True
            for req in mn.requisites:
                if len(set(req[0]).intersection(set(codes_))) < req[1]:
                    yes = False
                    break
            if yes:
                ret.append(mn.name)
        return ret
