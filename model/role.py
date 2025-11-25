from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import user_role_link#,role_permission_link

class Role(db.Model):
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, unique=True, nullable=False)

    users = relationship('User', secondary=user_role_link, back_populates='roles')

    def json(self):
        return {'id': self.role_id,
                'role_name': self.role_name}


    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"