import requests

req = requests.get('http://localhost:80/toDoList')

print(req.json())
