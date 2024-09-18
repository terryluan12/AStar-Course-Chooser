import mysql.connector
import requests
from requests.auth import HTTPBasicAuth
import json
import os

from dotenv import load_dotenv
load_dotenv()

# INSERT_COMMAND =    ("""
#                     INSERT INTO course (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     """,
#                       (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags))

# UPDATE_COMMAND = ("""
#                     UPDATE course
#                     SET prerequisite=%s, corequisite=%s, exclusion=%s, recommended_preparation=%s
#                     WHERE course_code = %s
#                     """,
#                     (prerequisite, corequisite, exclusion, recommended_preparation, course_code))

def insert_sql(): 
    host = os.environ.get("HOST_URL")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DATABASE")
    config = {"user": user, "password": password, "host": host, "database": database}
    
    connection = mysql.connector.connect(**config)
    with connection.cursor() as cursor, open("courses.json", "r") as reader:
        json_data = reader.read()
        data = json.loads(json_data)
        for datapoint in data:
            course_code = datapoint["course_code"]
            course_name = datapoint["course_name"]
            fixed_credit_value = float(datapoint.get("fixed_credit_value", -1))
            hours = datapoint.get("hours", None)
            description = datapoint.get("description", None)
            prerequisite = datapoint.get("prerequisite", None)
            corequisite = datapoint.get("corequisite", None)
            exclusion = datapoint.get("exclusion", None)
            recommended_preparation = datapoint.get("recommended_preparation", None)
            total_aus = datapoint.get("total_aus", None)
            program_tags = datapoint.get("program_tags", None)
            cursor.execute(
                """
                        INSERT INTO course (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_aus, program_tags)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                (
                    course_code,
                    course_name,
                    fixed_credit_value,
                    hours,
                    description,
                    prerequisite,
                    corequisite,
                    exclusion,
                    recommended_preparation,
                    total_aus,
                    program_tags,
                ),
            )
            connection.commit()

def insert_opensearch():
    # Define the URL and the payload
    url = os.environ.get("OPENSEARCH_URL")+"/courses/_bulk"
    username = os.environ.get("OPENSEARCH_USERNAME")
    password = os.environ.get("OPENSEARCH_PASSWORD")

    # Define the headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Define the authentication

    auth = HTTPBasicAuth(username, password)



    with open("courses.json", "r") as file:
        # Define the chunk size
        full_list = json.load(file)
        bulk_payload = ""

        for i, doc in enumerate(full_list, start=1):
            action = {"create": {"_index": "courses", "_id": str(i)}}
            bulk_payload += json.dumps(action) + "\n"
            bulk_payload += json.dumps(doc) + "\n"

        # Make the PUT request
        response = requests.post(url, headers=headers, auth=auth, data=bulk_payload)
        # Print the response
        print(response.status_code)
        # print(response.json())
        
# insert_sql()
insert_opensearch()