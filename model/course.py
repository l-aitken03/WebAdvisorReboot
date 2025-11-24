from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import course_user_link

class Course(db.Model):
    __tablename__ = 'course'

    class_id = Column(Integer, autoincrement=True, primary_key=True)
    course_id = Column(String(10), nullable=False)
    section_id = Column(Integer, nullable=False)
    course_title = Column(String(100), nullable=False)
    department = Column(String(50), nullable=False)
    campus = Column(String(20), nullable=False)
    term = Column(String(5), nullable=False)
    days_offered = Column(String(30), nullable=False)
    times_offered = Column(String(30), nullable=False)
    enroll_status = Column(Integer, nullable=False)
    # technically has tinyint(1) datatype, SQLite might try to interpret that as a boolean
    # enroll_status should support values of 0, 1, 2.
    credits = Column(Integer, nullable=False)

    users = relationship('User', secondary=course_user_link, back_populates='courses')
    '''users = relationship(
        "User",
        secondary=course_user_link,
        # lambda and absolute references added to fix PyCharm type checker complaining.
        # tldr: Python checks the datatypes and evaluates the secondaryjoin too early
            # and then defines it as a boolean instead of a SQLAlchemy boolean SQL expression.
        # the whole 'db.metadata.tables' thing works with __init__.py to avoid circular references
            # it's an absolute reference to the Object Relational Mapper's 'Metadata' dictionary of tables.
            # the 'foreign()' expression marks a field as the child foreign key side of the relationship
            # '.c' is an alias for the ORM columns collection and is used because
                # the relationship() join conditions expect column expressions, not Python variables
                # therefore, '.c' behaves like a dictionary mapping and an attributable object
        # I also added a 'type: ignore' flag to get PyCharm to actually shut up about it. It's hacky, but it works.
        primaryjoin=lambda: (
                (Course.course_id == foreign(course_user_link.c.course_id)) &
                (Course.section_id == foreign(course_user_link.c.section_id))
        ),
        secondaryjoin=lambda: db.metadata.tables["user"].c.user_id == foreign(course_user_link.c.user_id), # type: ignore
        back_populates='courses')'''

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
                'enroll_status': self.enroll_status,
                'credits': self.credits
                }

    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"