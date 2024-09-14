import mysql.connector
import json
import os

host = os.environ.get("HOST_URL")
user = os.environ.get("DB_USER")
password = user = os.environ.get("DB_PASSWORD")
database = os.environ.get("DATABASE")

db_config = {
  'user': user,
  'password': password,
  'host': host,
  'database': database
}

# CREATE_COMMAND = """CREATE TABLE course ( \
#             course_code VARCHAR(8) PRIMARY KEY, \
#             course_name VARCHAR(255) NOT NULL, \
#             credit_value INT NOT NULL, \
#             hours VARCHAR(255) NOT NULL, \
#             description TEXT NOT NULL, \
#             prerequisite VARCHAR(255), \
#             corequisite VARCHAR(255), \
#             exclusion VARCHAR(255), \
#             recommended_preparation VARCHAR(255), \
#             total_AUs VARCHAR(255), \
#             program_tags VARCHAR(255) NOT NULL)"""
# INSERT_COMMAND =    ("""
#                     INSERT INTO course (course_code, course_name, credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     """, 
#                       (course_code, course_name, credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags))

# UPDATE_COMMAND = ("""
#                     UPDATE course 
#                     SET prerequisite=%s, corequisite=%s, exclusion=%s, recommended_preparation=%s
#                     WHERE course_code = %s
#                     """,
#                     (prerequisite, corequisite, exclusion, recommended_preparation, course_code))

connection = mysql.connector.connect(**db_config)

with connection.cursor() as cursor, open('courses.json', 'r') as reader:
    json_data = reader.read()
    data = json.loads(json_data)
    for datapoint in data:
        course_code = "".join(datapoint['Course Code'])
        course_name = "".join(datapoint['Course Name'])
        credit_value = float(''.join(datapoint.get('Fixed Credit Value', ['0'])))
        hours = "".join(datapoint.get('Hours', []))
        description = "".join(datapoint.get('Description', []))
        prerequisite = " ".join(datapoint.get('Prerequisite', [])).replace(" . ", ". ").replace(" , ", ", ").replace(" / ", "/")
        corequisite = " ".join(datapoint.get('Corequisite', [])).replace(" . ", ". ").replace(" , ", ", ").replace(" / ", "/")
        exclusion = " ".join(datapoint.get('Exclusion', [])).replace(" . ", ". ").replace(" , ", ", ").replace(" / ", "/")
        recommended_preparation = " ".join(datapoint.get('Recommended Preparation', [])).replace(" , ", ", ").replace(" / ", "/")
        total_AUs = "".join(datapoint.get('Total AUs', []))
        program_tags = "".join(datapoint.get('Program Tags', []))
        cursor.execute(
                    """
                    INSERT INTO course (course_code, course_name, credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (course_code, course_name, credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags)
                )
        connection.commit()