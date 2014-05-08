from flaskboiler.data import Data, db
from flaskboiler.users.model import User


class UserData(Data):
    def __init__(self):
        super(UserData, self).__init__(User)

    def some_complicated_query(self, username):
        """
        Not actually a complicated query but this shows how we might want to mix raw SQL with SQLAlchemy ORM.
        """
        results = db.session.query(User).from_statement(
            """SELECT * FROM users WHERE username=:username"""
        ).params(username=username)

        return results
