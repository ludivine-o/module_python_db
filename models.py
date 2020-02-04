from peewee import *

db = MySQLDatabase('herboriste', user="ludivineo", password="CN-9564",  host="127.0.0.1")


class BaseModel(Model):
    class Meta:
        database = db


class SubClass(BaseModel):
    name = CharField()
    name_fr = CharField()
    class Meta:
        table_name = "sub_class"


class Indication(BaseModel):
    name = CharField()
    class Meta:
        table_name = "Indication"


class Usepart(BaseModel):
    name = CharField()


class Family(BaseModel):
    name = CharField()
    name_fr = CharField()
    sub_class = ForeignKeyField(SubClass, backref="sous_classes")


class Plante(BaseModel):
    name = CharField()
    price = DecimalField(10, 2)
    family = ForeignKeyField(Family, backref="plants")
    indication = ForeignKeyField(Indication, backref="indications")
    utilisation = ForeignKeyField(Usepart, column_name="use_part_id", backref="utilisations")




