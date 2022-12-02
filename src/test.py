from models import *

for user in User.select():
    print(user.username)
