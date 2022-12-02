from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource
from models import *


class ToDo(Resource):
    def get(self, title):
        toDo = ToDoEl.get_or_none(ToDoEl.title == title)
        if toDo:
            return toDo.__data__
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, title):
        data = request.get_json()
        toDo = ToDoEl.get_or_none(ToDoEl.title == title)
        if toDo:
            return {"message": "An item with title '{}' already exists.".format(title)}, 400
        toDo = ToDoEl(title=title, description=data["description"], done=data["done"])
        toDo.save()
        return toDo.__data__, 201

    @jwt_required()
    def delete(self, title):
        toDo = ToDoEl.get_or_none(ToDoEl.title == title)
        if toDo:
            toDo.delete_instance()
            return {"message": "Item deleted"}
        return {"message": "Item not found"}, 404

    @jwt_required()
    def put(self, title):
        data = request.get_json()
        toDo = ToDoEl.get_or_none(ToDoEl.title == title)
        if toDo:
            toDo.title = title
            toDo.description = data["description"]
            toDo.done = data["done"]
            toDo.save()
            return toDo.__data__
        return {"message": "Item not found"}, 404


class ToDoList(Resource):
    def get(self):
        return {"todos": [toDo.__data__ for toDo in ToDoEl.select()]}
