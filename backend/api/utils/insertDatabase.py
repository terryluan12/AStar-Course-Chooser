import mysql.connector
import requests
import json
import os
import boto3
import psycopg
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

from dotenv import load_dotenv

load_dotenv()

# DB credentials
host = os.environ.get("HOST_URL")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DATABASE")

# Opensearch credentials
opensearch_host = os.environ.get("OPENSEARCH_HOST")
port = os.environ.get("OPENSEARCH_PORT")
region = os.environ.get("AWS_REGION")


### POSTGRES COMMANDS
def create_postgres_table():
    config = {"user": user, "password": password, "host": host, "dbname": database}
    CREATE_COMMAND = """
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            course_code VARCHAR(20) NOT NULL,
            course_name TEXT NOT NULL,
            fixed_credit_value FLOAT DEFAULT -1,
            hours TEXT,
            description TEXT,
            prerequisite TEXT,
            corequisite TEXT,
            exclusion TEXT,
            recommended_preparation TEXT,
            total_aus TEXT,
            program_tags TEXT
        );
    """

    with psycopg.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_COMMAND)
        connection.commit()             

def insert_postgres():
    config = {"user": user, "password": password, "host": host, "dbname": database}
    with psycopg.connect(**config) as connection:
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
                            INSERT INTO courses (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_aus, program_tags)
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


### SQL COMMANDS
def insert_sql():
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
                INSERT INTO courses (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_aus, program_tags)
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

def execute_sql(command):
    config = {"user": user, "password": password, "host": host, "database": database}
    connection = mysql.connector.connect(**config)
    with connection.cursor() as cursor:

        cursor.execute(command)
        connection.commit()

### AWS COMMANDS
def insert_opensearch():
    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, region, "es")

    client = OpenSearch(
        hosts=[{"host": opensearch_host, "port": port}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        pool_maxsize=20,
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


create_postgres_table()
insert_postgres()

# INSERT_COMMAND =    ("""
#                     INSERT INTO courses (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                     """,
#                       (course_code, course_name, fixed_credit_value, hours, description, prerequisite, corequisite, exclusion, recommended_preparation, total_AUs, program_tags))

# UPDATE_COMMAND = ("""
#                     UPDATE courses
#                     SET prerequisite=%s, corequisite=%s, exclusion=%s, recommended_preparation=%s
#                     WHERE course_code = %s
#                     """,
#                     (prerequisite, corequisite, exclusion, recommended_preparation, course_code))
