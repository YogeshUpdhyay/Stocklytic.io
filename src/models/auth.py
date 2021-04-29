from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext
from src import Base

class User(Base):
    __tablename__ = 'users'
    fullname = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(fullname='%s', email='%s', password='%s')>" % (
                             self.fullname, self.email, self.password)
                            
    def setpassword(self, password):
        pass

    def verifypassword(self, password):
        pass