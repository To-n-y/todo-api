from peewee import *

db = SqliteDatabase('../db/database.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    username = CharField()
    password = CharField()

    class Meta:
        db_table = 'users'


class ToDoEl(BaseModel):
    title = CharField()
    description = CharField()
    done = BooleanField()

    class Meta:
        db_table = 'todos'
