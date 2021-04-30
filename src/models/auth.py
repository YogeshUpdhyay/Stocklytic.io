from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext
from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self):
        return "<User(fullname='%s', email='%s', password='%s')>" % (
                             self.fullname, self.email, self.password)
                            
    def setpassword(self, password):
        pass

    def verifypassword(self, password):
        pass