from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import user_role_link, user_course_link

class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_username = Column(String(255), unique=True, nullable=False)
    user_first_name = Column(String(50), nullable=False)
    user_last_name = Column(String(50), nullable=False)
    user_email = Column(String(254), unique=True, nullable=False)
    is_prof = Column(Boolean, nullable=False)
    is_student = Column(Boolean, nullable=False)

    roles = relationship('Role', secondary=user_role_link, back_populates='users')
<<<<<<< HEAD
    courses = relationship('Course', secondary=course_user_link, back_populates='users')
=======
    # extra arguments had to be defined because the Course table is uniquely difficult in that
        # it has a composite primary key and multiple linking foreign keys.
    # the course model has more documentation btw
    courses = relationship(
        "Course",
        secondary=user_course_link,
        primaryjoin=lambda: User.user_id == foreign(user_course_link.c.user_id),
        secondaryjoin=lambda: (
                (foreign(user_course_link.c.course_id) == db.metadata.tables["course"].c.course_id) &
                (foreign(user_course_link.c.section_id) == db.metadata.tables["course"].c.section_id)
        ),
        back_populates='users')
>>>>>>> main

    def json(self):
        return {'id': self.user_id,
                'username': self.user_username,
                'first_name': self.user_first_name,
                'last_name': self.user_last_name,
                'email': self.user_email,
                'is_prof': self.is_prof,
                'is_student': self.is_student}

    def __repr__(self):
        # vars(self) returns a dictionary of all instance attributes, .items() returns key/value pairs
        # this joins a formatted list of instance attribute key value pairs
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"