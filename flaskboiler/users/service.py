from flaskboiler.service import Service
from flaskboiler.users.data import UserData


class UserService(Service):
    def __init__(self):
        super(UserService, self).__init__(UserData())
