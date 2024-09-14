from mongoengine import Document, StringField, ListField, DictField


class Wishlist(Document):
    username = StringField(required=True, unique=True)
    course = ListField(StringField())
    comments = DictField()

    @classmethod
    def create(cls, username_):
        usr = cls.objects(username=username_)
        usr.update_one(set__course=[], upsert=True)
        return True

    def add_course(self, course_):
        if course_ not in self.course:
            self.update(add_to_set__course=course_)

    def remove_course(self, course_):
        if course_ in self.course:
            self.course.remove(course_)
            self.save()

    def expand(self):
        ret = {
            "username": self.username,
            "course": self.course,
            "comments": self.comments,
        }
        return ret
