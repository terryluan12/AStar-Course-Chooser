from flask import request
from flask_restx import Namespace, Resource
from api.models.Course import Course
from requests.auth import HTTPBasicAuth
from nysiis import nysiis
import re

api = Namespace('Course', description='Course related operations')

@api.route('/course')
class CourseView(Resource):
    @api.doc(params={'code': 'Course code'})
    @api.doc(responses={200: 'Course Found'})
    def get(self):
        # TODO Implement Fuzzy Searching
        resp = {}
        courses = []
        input = request.args.get("code")
        codes = re.findall("[a-zA-Z]{3}\d{3}[a-zA-Z]?\d?", input)
        if codes:
            for code in codes:
                code = code.upper()
                if len(code) == 6:
                    code += "[A-Z][0-9]"
                elif len(code) == 5:
                    code += "[0-9]"
                courses.extend(Course.get(code))
        courses.extend(Course.get(input + '*'))
        resp["message"] = "Course search success"
        resp["courses"] = [course.to_json() for course in courses]
        return resp, 200
                
@api.route('/course/search')
class CourseSearchView(Resource):
    @api.doc(params={'code': 'Course code'})
    @api.doc(responses={200: 'Course Found'})
    def get(self):
        # TODO Implement Fuzzy Searching
        resp = {}
        courses = Course.search(request.args.get("code"))
        resp["message"] = "Course search success"
        resp["courses"] = courses
        return resp, 200
        
# class ShowCourseGraph(Resource):
#     def get(self):
#         code = request.args.get('code')
#         if not Course.objects(code=code):
#             resp = jsonify({'message': f"Course {code} doesn't exist"})
#             resp.status_code = 404
#             return resp
#         try:
#             resp = jsonify({'graph': Course.get_requisite_graph(code)})
#             resp.status_code = 200
#             return resp
#         except Exception as e:
#             resp = jsonify({'error': 'something went wrong'})
#             resp.status_code = 400
#             return resp

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('code', required=True)
#         data = parser.parse_args()
#         code = data['code']
#         if not Course.objects(code=code):
#             resp = jsonify({'message': f"Course {code} doesn't exist"})
#             resp.status_code = 404
#             return resp
#         try:
#             resp = jsonify({'graph': Course.get_requisite_graph(code)})
#             resp.status_code = 200
#             return resp
#         except Exception as e:
#             resp = jsonify({'error': 'something went wrong'})
#             resp.status_code = 400
#             return resp
