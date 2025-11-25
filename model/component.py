from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import component_permission_link

class Component(db.Model):
    __tablename__ = 'Component'

    comp_id = Column(Integer, primary_key=True, nullable=False)
    comp_name = Column(String, nullable=False)
    comp_type = Column(Integer, nullable=False)

    permissions = relationship('Permission', secondary=component_permission_link, back_populates='components')


    def json(self):
        return {'id': self.comp_id,
                'name': self.comp_name,
                'type': self.comp_type}


    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"