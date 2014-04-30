from datetime import datetime
from flaskboiler import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(128))
    last_name = db.Column(db.Unicode(128))
    username = db.Column(db.Unicode(32))
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username
