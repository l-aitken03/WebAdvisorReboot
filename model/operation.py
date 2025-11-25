from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import operation_permission_link

class Operation(db.Model):
    __tablename__ = 'Operation'

    op_id = Column(Integer, primary_key=True, nullable=False)
    op_route = Column(String, nullable=False)
    op_type = Column(Integer, nullable=False)

    permissions = relationship('Permission', secondary=operation_permission_link, back_populates='operations')


    def json(self):
        return {'id': self.op_id,
                'route': self.op_route,
                'type': self.op_type}


    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"