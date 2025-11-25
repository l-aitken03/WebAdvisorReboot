from sqlalchemy import Table, Column, ForeignKey, Integer
from model.base import db

user_role_link = Table(
    'user_role_link', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
         Column('role_id', Integer, ForeignKey('role.role_id'), primary_key=True)
)

<<<<<<< HEAD
course_user_link = Table(
    'course_user_link', db.Model.metadata,
    Column('class_id', Integer, ForeignKey('course.class_id'), autoincrement=True, primary_key=True),
        Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True)
=======
user_course_link = Table(
    'user_course_link', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('course.course_id'), primary_key=True),
        Column('section_id', Integer, ForeignKey('course.section_id'), primary_key=True)
>>>>>>> main
)