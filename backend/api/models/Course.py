# This is the model

from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import String, Index
from api.models.Wishlist import Wishlist
from api.utils.database import sql_db
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match


class Course(sql_db.Model):
    course_code: Mapped[str] = mapped_column(String(10), primary_key=True)
    course_name: Mapped[str] = mapped_column(String(100))
    credit_value: Mapped[float]
    hours: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(300))
    prerequisite: Mapped[str] = mapped_column(String(150))
    corequisite: Mapped[str] = mapped_column(String(150))
    exclusion: Mapped[str] = mapped_column(String(150))
    recommended_preparation: Mapped[str] = mapped_column(String(150))
    total_aus: Mapped[str] = mapped_column(String(100))
    program_tags: Mapped[str] = mapped_column(String(100))
    subscribed_users = relationship('User', secondary=Wishlist.__table__, back_populates='wished_courses')

    __table_args__ = (
        Index('course_code_index', 'course_code', mysql_prefix='FULLTEXT'),
    )
    
    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_aus}, program_tags={self.program_tags})"

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
