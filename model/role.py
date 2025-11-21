from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from .associations import user_role_link

#from .base import Base
from .base import db

class Role(db.Model):
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, unique=True, nullable=False)

    users = relationship('User', secondary=user_role_link, back_populates='roles')

    def json(self):
        return {'id': self.role_id,
                'role_name': self.role_name}


    def __repr__(self):
        return f"<Role(id={self.role_id}, name={self.role_name})>"