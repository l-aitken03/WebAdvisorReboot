from sqlalchemy import Table, Column, ForeignKey, Integer
from model.base import db

user_role_link = Table(
    'user_role_link', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
         Column('role_id', Integer, ForeignKey('role.role_id'), primary_key=True)
)

course_user_link = Table(
    'course_user_link', db.Model.metadata,
    Column('class_id', Integer, ForeignKey('course.class_id'), autoincrement=True, primary_key=True),
        Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True)
)

role_permission_link = Table(
    'role_perm_link', db.Model.metadata,
    Column('role_id', Integer, ForeignKey('Role.role_id'), primary_key=True),
    Column('perm_id', Integer, ForeignKey('Permission.perm_id'), primary_key=True)
)

operation_permission_link = Table (
    'oprn_perm_link', db.Model.metadata,
    Column('op_id', Integer, ForeignKey('Operation.op_id'), primary_key=True),
    Column('perm_id', Integer, ForeignKey('Permission.perm_id'), primary_key=True)
)

component_permission_link = Table (
    'comp_perm_link', db.Model.metadata,
    Column('comp_id', Integer, ForeignKey('Component.comp_id'), primary_key=True),
    Column('perm_id', Integer, ForeignKey('Permission.perm_id'), primary_key=True)
)