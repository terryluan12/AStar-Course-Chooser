from api.utils.database import sql_db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String


class Minor(sql_db.Model):
    name: Mapped[str] = mapped_column(String(50), primary_key=True)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    requisites: Mapped[str] = mapped_column(String(200), nullable=False)

    @classmethod
    def get(cls, name):
        return cls.objects(name=name).get()

    @classmethod
    def check(cls, codes):
        ret = []

        for mn in cls.objects:
            yes = True
            for req in mn.requisites:
                if len(set(req[0]).intersection(set(codes))) < req[1]:
                    yes = False
                    break
            if yes:
                ret.append(mn)
        return ret
