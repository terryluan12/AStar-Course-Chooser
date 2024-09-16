# This is the model

from sqlalchemy.orm import relationship, mapped_column, Mapped
from api.models.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match


class Course(sql_db.Model):
    course_code: Mapped[str] = mapped_column(primary_key=True)
    course_name: Mapped[str]
    credit_value: Mapped[float]
    hours: Mapped[str]
    description: Mapped[str]
    prerequisite: Mapped[str]
    corequisite: Mapped[str]
    exclusion: Mapped[str]
    recommended_preparation: Mapped[str]
    total_aus: Mapped[str]
    program_tags: Mapped[str]

    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_AUs}, program_tags={self.program_tags})"

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
        )
        return [course._mapping["Course"].to_json() for course in courses]
