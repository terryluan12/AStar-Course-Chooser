from mongoengine import Document, StringField, ListField


class Minor(Document):
    name = StringField(required=True, unique=True)
    description = StringField()
    requisites = ListField(ListField(ListField()))
    # [ (['code', 'code'], 2), (['code', 'code'], 1), ]

    @classmethod
    def get(cls, name_):
        return cls.objects(name=name_).get()

    @classmethod
    def check(cls, codes_):
        ret = []

        for mn in cls.objects:
            print(f"checking {mn}")
            yes = True
            for req in mn.requisites:
                if len(set(req[0]).intersection(set(codes_))) < req[1]:
                    yes = False
                    break
            if yes:
                ret.append(mn)
        return ret
