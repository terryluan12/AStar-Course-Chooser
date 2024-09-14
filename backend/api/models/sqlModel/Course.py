# This is the model

from sqlalchemy.orm import mapped_column, Mapped
from api.utils.database import sql_db


class Course(sql_db.Model):
    __table__ = sql_db.metadata.tables["course"]
    # __tablename__ = "course"
    # __mapper_args__ = {'column_prefix':'_'}

    # code: Mapped[str] = mapped_column("code", primary_key=True)
    # name: Mapped[str] = mapped_column()
    # credit_value: Mapped[float] = mapped_column()
    # hours: Mapped[str] = mapped_column()
    # description: Mapped[str] = mapped_column()
    # prereq: Mapped[str] = mapped_column()
    # coreq: Mapped[str] = mapped_column()
    # exclusion: Mapped[str] = mapped_column()
    # rec_prep: Mapped[str] = mapped_column()
    # total_au: Mapped[str] = mapped_column()
    # program_tags: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credit_value={self.credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prerequisite}, corequisite={self.corequisite}, exclusion={self.exclusion}, recommended_preparation={self.recommended_preparation}, total_au={self.total_AUs}, program_tags={self.program_tags})"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # @classmethod
    # def get(cls, code_):
    #     return cls.query.filter_by(code=code_).first()
