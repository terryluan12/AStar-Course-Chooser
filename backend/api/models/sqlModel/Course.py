# This is the model

from sqlalchemy.orm import mapped_column, Mapped
from api.utils.database import sql_db
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match


class Course(sql_db.Model):
    course_code: Mapped[str] = mapped_column( primary_key=True)
    course_name: Mapped[str] = mapped_column()
    credit_value: Mapped[float] = mapped_column()
    hours: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    prerequisite: Mapped[str] = mapped_column()
    corequisite: Mapped[str] = mapped_column()
    exclusion: Mapped[str] = mapped_column()
    recommended_preparation: Mapped[str] = mapped_column()
    total_aus: Mapped[str] = mapped_column()
    program_tags: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_AUs}, program_tags={self.program_tags})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get(cls, code_):
        match_expr = match(
                Course.course_code,
                against=code_,
            )
        courses = sql_db.session.execute(
            sql_db.select(Course)
            .where(match_expr.in_boolean_mode())
            .order_by(desc(match_expr))
            .limit(10)
        )
        return [course._mapping["Course"].to_json() for course in courses]
