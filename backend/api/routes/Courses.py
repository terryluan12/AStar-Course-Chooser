from flask import jsonify, request
from flask_restx import Resource, reqparse
import json
from api.utils.database import sql_db
from api.models.sqlModel.Course import Course
from nysiis import nysiis
import re
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match


# -------------------- Course related --------------------
class SearchCourse(Resource):
    def get(self):
        input = request.args.get("input")
        code = re.findall("[a-zA-Z]{3}\d{3}[hH]?\d?", input)
        if code:
            code = code[0].upper()
            if len(code) == 6:
                code += "H1"
            elif len(code) == 5:
                code += "1"
            course = sql_db.get_or_404(Course, code)
            if course:
                try:
                    resp = jsonify({"course": course.to_json()})
                    resp.status_code = 200
                    return resp
                except Exception as e:
                    resp = jsonify({"error": e})
                    resp.status_code = 400
                    return resp
        # input = ' '.join([nysiis(w) for w in input.split()])
        try:
            match_expr = match(
                Course.course_code,
                against=input + "*",
            )
            search = sql_db.session.execute(
                sql_db.select(Course)
                .where(match_expr.in_boolean_mode())
                .order_by(desc(match_expr))
                .limit(10)
            )
            results = [course._mapping["Course"].to_json() for course in search]
            resp = jsonify({"courses": results})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp


class ShowCourse(Resource):
    def get(self):
        code = request.args.get("code")
        course = sql_db.get_or_404(Course, code)
        if not course:
            resp = jsonify({"message": f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp
        try:
            resp = jsonify({"course": course.to_json()})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": "something went wrong"})
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
