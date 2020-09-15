from .model import db
from datetime import datetime

class Keeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    kid = db.Column(db.Integer, db.ForeignKey('kinda.id'), nullable=False)
    price = db.Column(db.Integer)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)



    def __init__(self, id, user, kinda, price):
        self.id = id
        self.user = user
        self.kinda = kinda
        self.price = price
