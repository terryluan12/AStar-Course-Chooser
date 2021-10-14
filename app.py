# this is the flask core
#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# MongoDB URI
DB_URI = "mongodb+srv://Cansin:cv190499@a-star.roe6s.mongodb.net/A-Star?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)

class Course(db.Document):
    courseName = db.StringField()
    courseCode = db.StringField()
    def to_json(self):
        return {"courseName": self.courseName,
                "courseCode": self.courseCode}

# @app.route('/', methods=['GET'])
# def query_records():
#     courseName = request.args.get('name')
#     course = Course.objects(courseName=courseName).first()
#     if not course:
#         return jsonify({'error': 'data not found'})
#     else:
#         return jsonify(course.to_json())

# this saves to db
Course(courseName='Software Engineering', courseCode='ECE444').save()



if __name__ == '__main__':
    app.run()