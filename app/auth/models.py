from flask_login import UserMixin
from .. import db, login_manager
from sqlalchemy import Column, Integer, String, LargeBinary
from passlib.hash import pbkdf2_sha256

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    def check_password(self, password):
        return pbkdf2_sha256.verify(password, bytes(self.password))
    
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    return user if user else None