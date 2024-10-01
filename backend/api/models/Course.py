from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import String, Index
from api.models.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy.dialects.mysql import match
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3
import json
import os

from dotenv import load_dotenv

load_dotenv()


class Course(sql_db.Model):
    course_code: Mapped[str] = mapped_column(String(10), primary_key=True)
    course_name: Mapped[str] = mapped_column(String(100))
    fixed_credit_value: Mapped[float]
    hours: Mapped[str] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(String(300))
    prerequisite: Mapped[str] = mapped_column(String(150), nullable=True)
    corequisite: Mapped[str] = mapped_column(String(150), nullable=True)
    exclusion: Mapped[str] = mapped_column(String(150), nullable=True)
    recommended_preparation: Mapped[str] = mapped_column(String(150), nullable=True)
    total_aus: Mapped[str] = mapped_column(String(100), nullable=True)
    program_tags: Mapped[str] = mapped_column(String(100), nullable=True)
    subscribed_users = relationship(
        "User", secondary=Wishlist.__table__, back_populates="wished_courses"
    )

    __table_args__ = (
        Index("course_code_index", "course_code", mysql_prefix="FULLTEXT"),
    )

    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.fixed_credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_aus}, program_tags={self.program_tags})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get(cls, code):
        course = sql_db.session.execute(
            sql_db.select(Course).where(cls.course_code.regexp_match(code))
        ).scalar()
        return course

    @classmethod
    def put(cls, course_code, course_name, fixed_credit_value, description):
        course = cls(course_code=course_code, course_name=course_name, fixed_credit_value=fixed_credit_value, description=description)
        sql_db.session.add(course)
        sql_db.session.commit()
        return True

    @classmethod
    def search(cls, query):
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
            pool_maxsize=20,
        )

        payload = json.dumps(
            {
                "size": 10,
                "query": {
                    "query_string": {
                        "query": query,
                        "fields": [
                            "course_code^3.0",
                            "course_name",
                            "description^2.0",
                            "prerequisite",
                            "corequisite",
                            "exclusion",
                            "recommended_preparation",
                            "program_tags",
                        ],
                    }
                },
            }
        )
        results = client.search(index="courses", body=payload).get("hits").get("hits")
        courses = [course.get("_source") for course in results]
        return courses
