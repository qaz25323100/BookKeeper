from .model import db


class Kinda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kindas = db.Column(db.String(5))

    db_kinda_keeper = db.relationship(
        'Keeper',
        backref='kinda',
        lazy='dynamic'
    )

    def __init__(self, kindas):
        self.kindas = kindas
