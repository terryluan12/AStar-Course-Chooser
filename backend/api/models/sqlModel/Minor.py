from api.utils.database import sql_db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String


class Minor(sql_db.Model):
    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    requisites: Mapped[str] = mapped_column(String(200), nullable=False)

    @classmethod
    def get(cls, name_):
        return cls.objects(name=name_).get()

    @classmethod
    def check(cls, codes_):
        ret = []

        for mn in cls.objects:
            yes = True
            for req in mn.requisites:
                if len(set(req[0]).intersection(set(codes_))) < req[1]:
                    yes = False
                    break
            if yes:
                ret.append(mn)
        return ret
