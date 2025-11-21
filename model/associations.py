from sqlalchemy import Table, Column, ForeignKey, Integer

#from model.base import Base
from model.base import db

user_role_link = Table(
    'user_role_link', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
         Column('role_id', Integer, ForeignKey('role.role_id'), primary_key=True)
)