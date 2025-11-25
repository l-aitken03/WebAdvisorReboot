from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import role_permission_link, operation_permission_link, component_permission_link

class Permission(db.Model):
    __tablename__ = 'permission'

    perm_id = Column(Integer, primary_key=True, nullable=False)
    perm_name = Column(String, unique=True, nullable=False)
    # perm_name is nullable and not unique in the SQLite version currently; this will be fixed when I regenerate the db.

    roles = relationship('Role', secondary=role_permission_link, back_populates='permissions')
    operations = relationship('Operation', secondary=operation_permission_link, back_populates='permissions')
    components = relationship('Component', secondary=component_permission_link, back_populates='permissions')


    def json(self):
        return {'id': self.perm_id,
                'perm_name': self.perm_name}


    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"