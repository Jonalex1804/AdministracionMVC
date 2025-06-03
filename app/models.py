from . import db
from flask_login import UserMixin
from datetime import date

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class PersonDebt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    abono = db.Column(db.Float, nullable=False, default=0.0)
    due_date = db.Column(db.Date, nullable=True)

    @property
    def estado(self):
<<<<<<< HEAD
        if self.abono == 0:
            return 'incumplido'
=======
>>>>>>> d97651a80dbbcd304d728757b633b57fcea39c18
        if self.abono >= self.amount:
            return 'cumplido'
        elif self.due_date and date.today() > self.due_date:
            return 'moroso'
        else:
            return 'pendiente'