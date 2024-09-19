import mysql.connector
import requests
import json
import os
import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

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
    
    opensearch_host = os.environ.get("OPENSEARCH_HOST")
    port = os.environ.get("OPENSEARCH_PORT")
    region = os.environ.get("AWS_REGION")
    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, region, "es")

    client = OpenSearch(
        hosts=[{"host": opensearch_host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        pool_maxsize = 20
    )
    with open("courses.json", "r") as file:
        full_list = json.load(file)
        bulk_payload = ""

        for i, doc in enumerate(full_list, start=1):
            action = {"create": {"_index": "courses", "_id": str(i)}}
            bulk_payload += json.dumps(action) + "\n"
            bulk_payload += json.dumps(doc) + "\n"

        response = client.bulk(body=bulk_payload)
        print(response.status_code)
        

def execute_sql(command): 
    host = os.environ.get("HOST_URL")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DATABASE")
    config = {"user": user, "password": password, "host": host, "database": database}
    
    connection = mysql.connector.connect(**config)
    with connection.cursor() as cursor:
        
        cursor.execute(command
        )
        connection.commit()

# execute_sql("SHOW tables")
# execute_sql("DROP TABLE wishlist")
# execute_sql("DROP TABLE session")
# execute_sql("DROP TABLE user")

# insert_sql()
# insert_opensearch()