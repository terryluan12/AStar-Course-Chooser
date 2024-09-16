from flask import jsonify, request
from flask_restx import Namespace, Resource, reqparse, fields
from api.utils.database import sql_db
from api.models.Course import Course
from nysiis import nysiis
import re

api = Namespace('Course', description='Course related operations')

model = api.model('Course', {
    'course_code': fields.String,
    'course_name': fields.String,
    'credit_value': fields.String,
    'hours': fields.String,
    'description': fields.String,
    'prerequisite': fields.String,
    'corequisite': fields.String,
    'exclusion': fields.String,
    'recommended_preparation': fields.String,
    'total_aus': fields.String,
    'program_tags': fields.String,
})

@api.route('/course')
class CourseView(Resource):
    
    @api.doc(params={'code': 'Course code'})
    @api.doc(responses={404: 'Course not found'})
    @api.marshal_with(model, code=200, description='Course found')
    def get(self):
        input = request.args.get("code")
        codes = re.findall("[a-zA-Z]{3}\d{3}[a-zA-Z]?\d?", input)
        print(f'codes is {codes}')
        print(f'input is  is {input}')
        if codes:
            for code in codes:
                code = code.upper()
                if len(code) == 6:
                    code += "[A-Z][0-9]"
                elif len(code) == 5:
                    code += "[0-9]"
                courses = Course.get(code) # add 400 error
                try:
                    resp = jsonify({"courses": courses})
                    resp.status_code = 200
                    return resp
                except Exception as e:
                    resp = jsonify({"error": e})
                    resp.status_code = 400
                    return resp
        else:
            # TODO Implement Fuzzy Searching
            courses = Course.get(input + '*')
            try:
                resp = jsonify({"courses": courses})
                resp.status_code = 200
                return resp
            except Exception as e:
                resp = jsonify({"error": e})
                resp.status_code = 400
                return resp


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
