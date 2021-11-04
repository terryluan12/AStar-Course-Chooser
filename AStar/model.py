from app import app, db

class Course(db.Document):
    code = db.StringField()
    name = db.StringField()
    description = db.StringField()
    prereq = db.ListField()
    coreq = db.ListField()
    exclusion = db.ListField()
    keyword = db.ListField()
