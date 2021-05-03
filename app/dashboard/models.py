from .. import db
from sqlalchemy import Column, String, Integer

class Stock(db.Model):

    __tablename__ = 'Stock'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True)