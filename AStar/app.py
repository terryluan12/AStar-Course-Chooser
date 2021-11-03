# this is the flask core
#!/usr/bin/env python3
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
import json

global app
app = Flask(__name__)

# MongoDB URI
DB_URI = "mongodb+srv://Cansin:cv190499@a-star.roe6s.mongodb.net/A-Star?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

global db
db = MongoEngine(app)

class Course(db.Document):
    name = db.StringField()
    code = db.StringField()
    description = db.StringField()
    prereq = db.StringField()
    coreq = db.StringField()
    exclusion = db.StringField()

    def to_json(self):
        return {"Name": self.name,
                "Code": self.code,
                "Description": self.description,
                "Prerequisite": self.prereq,
                "Corequisite": self.coreq,
                "Exclusion": self.exclusion}
    def __str__(self):
        return "{} ({}):\n{}\nPreRequisites: {}    Corequisites: {}    Exclusions: {}".format(self.name, self.code, self.description, self.prereq, self.coreq, self.exclusion)

@app.route("/")
def app_connect():
    return "A-Star"

# @app.route('/', methods=['GET'])
# def query_records():
#     courseName = request.args.get('name')
#     course = Course.objects(courseName=courseName).first()
#     if not course:
#         return jsonify({'error': 'data not found'})
#     else:
#         return jsonify(course.to_json())

# this saves to db
#Course(courseName='Software Engineering', courseCode='ECE444').save()



if __name__ == '__main__':
    with open("test.json") as f:
        data = json.load(f)
    for i in range(75):
        i = str(i)
        Course(name=data["name"][i], code=data["code"][i], description=data["description"][i], prereq=data["prereq"][i], coreq=data["coreq"][i], exclusion=data["exclusion"][i]).save()

    
