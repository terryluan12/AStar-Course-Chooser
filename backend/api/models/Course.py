# This is the model

from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import String, Index
from api.models.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match
from opensearchpy import OpenSearch, RequestsHttpConnection
import boto3
import json
from requests.auth import HTTPBasicAuth
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
    subscribed_users = relationship('User', secondary=Wishlist.__table__, back_populates='wished_courses')

    __table_args__ = (
        Index('course_code_index', 'course_code', mysql_prefix='FULLTEXT'),
    )
    
    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.fixed_credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_aus}, program_tags={self.program_tags})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get(cls, code):
        match_expr = match(
                Course.course_code,
                against=code,
            )
        courses = sql_db.session.execute(
            sql_db.select(Course)
            .where(match_expr.in_boolean_mode())
            .order_by(desc(match_expr))
            .limit(10)
        ).scalars().all()
        return courses if courses else []

    @classmethod
    def search(cls, query):
        opensearch_host = os.environ.get("OPENSEARCH_HOST")
        # region = os.environ.get("AWS_REGION")
        # service = "es"
        # credentials = boto3.Session().get_credentials()
        # auth
        username = os.environ.get("OPENSEARCH_USERNAME")
        password = os.environ.get("OPENSEARCH_PASSWORD")
        auth = HTTPBasicAuth(username, password)
        client = OpenSearch(
            hosts=[{"host": opensearch_host, "port": 443}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        payload = json.dumps({
            "size": 10,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["course_code^3.0", "course_name", "description^2.0", "prerequisite", "corequisite", "exclusion", "recommended_preparation", "program_tags"]
                    }
            }
        })
        
        results = client.search(index="courses", body=payload).get("hits").get("hits")
        courses = [course.get("_source") for course in results]
        return courses