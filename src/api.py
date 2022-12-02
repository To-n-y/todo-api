from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from handlers import ToDo, ToDoList
from security import auth, identity
from user import SignUp
import dbstart

dbstart.start()

app = Flask(__name__)
api = Api(app)
app.secret_key = "101"
jwt = JWT(app, auth, identity)

if __name__ == '__main__':
    api.add_resource(ToDo, '/toDoList/<string:title>')
    api.add_resource(ToDoList, '/toDoList')
    api.add_resource(SignUp, '/signup')
    app.run(host="0.0.0.0", port=80, debug=True)
