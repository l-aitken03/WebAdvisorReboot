from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from .associations import user_role_link

from .base import Base

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_username = Column(String(255), unique=True, nullable=False)
    user_first_name = Column(String(50), nullable=False)
    user_last_name = Column(String(50), nullable=False)
    user_email = Column(String(254), unique=True, nullable=False)
    is_prof = Column(Boolean, nullable=False)
    is_student = Column(Boolean, nullable=False)

    roles = relationship('Role', secondary=user_role_link, back_populates='users')

    def json(self):
        return {'id': self.user_id,
                'username': self.user_username,
                'first_name': self.user_first_name,
                'last_name': self.user_last_name,
                'email': self.user_email,
                'is_prof': self.is_prof,
                'is_student': self.is_student}

    def __repr__(self):
        return f"<User(id={self.user_id}, username={self.user_username})>"
