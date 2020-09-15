from .model import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10))
    pwd = db.Column(db.String(40))
    name = db.Column(db.String(12))

    db_user_keeper = db.relationship(
        'Keeper',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, phone, pwd, name):
        self.phone = phone
        self.pwd = pwd
        self.name = name
