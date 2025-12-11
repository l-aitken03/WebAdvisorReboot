from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from enum import IntEnum
from model.base import db
from model.associations import course_user_link

# Class to translate Integers into human-readable course enrollment status codes.
class EnrollStatus(IntEnum):
    Open = 0
    Waitlisted = 1
    Closed = 2

class Course(db.Model):
    __tablename__ = 'course'

    class_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=False)
    section_id = Column(Integer, primary_key=False)
    course_title = Column(String(100), nullable=False)
    department = Column(String(50), nullable=False)
    campus = Column(String(20), nullable=False)
    term = Column(String(5), nullable=False)
    days_offered = Column(String(30), nullable=False)
    times_offered = Column(String(30), nullable=False)
    enroll_status = Column(Integer, nullable=False) # Translated/Enumerated via EnrollStatus class and enroll_status_label function.
    credits = Column((Numeric(2,1)), nullable=False)

    users = relationship("User", secondary=course_user_link, back_populates='courses')

    def enroll_status_label(self):
        return EnrollStatus(self.enroll_status).name.title()

    def json(self):
        return {'class_id': self.class_id,
                'course_id': self.course_id,
                'section_id': self.section_id,
                'course_title': self.course_title,
                'department': self.department,
                'campus': self.campus,
                'term': self.term,
                'days_offered': self.days_offered,
                'times_offered': self.times_offered,
                'enroll_status': self.enroll_status_label(),
                'credits': self.credits
                }

    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"