# This is the model

from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from index import sql_db

class Course(sql_db.Model):
  __tablename__ = "course"

  code: Mapped[str] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column()
  credit_value: Mapped[float] = mapped_column()
  hours: Mapped[str] = mapped_column()
  description: Mapped[str] = mapped_column()
  prereq: Mapped[str] = mapped_column()
  coreq: Mapped[str] = mapped_column()
  exclusion: Mapped[str] = mapped_column()
  rec_prep: Mapped[str] = mapped_column()
  total_au: Mapped[str] = mapped_column()
  program_tags: Mapped[str] = mapped_column()
  
  def __repr__(self) -> str:
    return f"Course(course_code={self.code}, course_name={self.name}, credit_value={self.credit_value}, hours={self.hours}, description={self.description}, prerequisite={self.prereq}, corequisite={self.coreq}, exclusion={self.exclusion}, recommended_preparation={self.rec_prep}, total_au={self.total_au}, program_tags={self.program_tags})"
  
  @classmethod
  def get(cls, code_):
      return cls.query.filter_by(code=code_).first()
