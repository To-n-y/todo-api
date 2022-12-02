from models import *


def start():
    with db:
        db.create_tables([User, ToDoEl])

        ToDoEl.get_or_create(title='Buy_milk', description='Buy milk from the store', done=False)
        ToDoEl.get_or_create(title='Walk_the_dog', description='Take the dog for a walk', done=False)
        ToDoEl.get_or_create(title='Water_the_plants', description='Water the plants in the garden', done=False)

        User.get_or_create(username='admin', password='admin')
        User.get_or_create(username='user', password='user')
