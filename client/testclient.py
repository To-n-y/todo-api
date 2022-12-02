import requests

req = requests.get('http://localhost:80/toDoList')
req2 = requests.get('http://localhost:80/toDoList/Buy_milk')

print(req.json())
print(req2.json())
