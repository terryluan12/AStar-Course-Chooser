from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
  pass


sql_db = SQLAlchemy(model_class=Base)