from flask.ext.testing import TestCase

from flaskboiler import create_app, db
from flaskboiler.users.service import UserService

class UserServiceTest(TestCase):

    def create_app(self):
        # pass in test configuration
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_asdf(self):
        user_service = UserService()
        reek = user_service.create(first_name='theon', last_name='greyjoy', username='reek')
        kingslayer = user_service.create(first_name='jaime', last_name='lannister', username='kingslayer')
        dwarf = user_service.create(first_name='tyrion', last_name='lannister', username='dwarf')
        jon = user_service.create(first_name='jon', last_name='snow', username='bastard')

        user1 = user_service.get(1)
        user2 = user_service.get(2)

        users = user_service.find(username='reek')
        users = user_service.find(last_name='lannister')

        users = user_service.update(dwarf, username='scarface')

        user_service._data.some_complicated_query("scarface")

        print 'done'
