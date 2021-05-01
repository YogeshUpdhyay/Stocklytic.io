from flask_login import UserMixin
from .. import db, login_manager
from sqlalchemy import LargeBinary, Column, Integer, String

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(LargeBinary)

