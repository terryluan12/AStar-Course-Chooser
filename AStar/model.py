# This is the model

from config import app, db

class Course(db.Document):
    code = db.StringField(required=True, primary_key=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    syllabus = db.URLField()
    prereq = db.ListField()
    coreq = db.ListField()
    exclusion = db.ListField()
    keyword = db.ListField(required=True)

    @classmethod
    def get(cls, code_):
        return cls.objects(code=code_)
    
    @classmethod
    def get_requisite_graph(cls, code_):
        # TODO
        return

class Wishlist(db.Document):
    name = db.StringField()
    course = db.ListField(Course)

    def add_course(self, code_):
        self.course += [code_]
    
    def remove_course(self, code_):
        if code_ in self.course:
            self.course.remove(code_)


class User(db.Document):
    username = db.StringField(primary_key=True)
    password = db.StringField(required=True)
    comments = db.DictField()
    wishlist = db.ReferenceField(Wishlist)

    @classmethod
    def create(cls, username_, password_):
        cls(username=username_, password=password_).save()

    @classmethod
    def delete(cls, username_):
        cls(username=username_).delete()

    @classmethod
    def verify_password(cls, username_, password_) -> bool:
        usr = cls(username=username_)
        if usr.password == password_:
            return True
        return False
    
    @classmethod
    def get_wishlist(cls, username_):
        return Wishlist(_id=cls(username=username_).wishlist)

    @classmethod
    def add_comment(cls, username_, code_, comment_):
        usr = cls(username=username_)
        usr.comments[code_] = comment_
        usr.save()


class Minor(db.Document):
    name = db.StringField(primary_key=True)
    description = db.StringField
    requisites = db.ListField(db.ListField(db.ListField)) 
            #[ (['code', 'code'], 2), (['code', 'code'], 1), ] 

    @classmethod
    def get(cls, name_):
        return cls(name=name_)
    
    @classmethod
    def check(cls, codes_):
        ret = []
        for mn in cls.objects:
            yes = True
            for req in mn.requisites:
                if len(set(req[0]).intersection(set(codes_))) < req[1]:
                    yes = False
                    break
            if yes:
                ret.append(mn.name)
        return ret
