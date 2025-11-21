from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from model.user import User
from model.role import Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///../webadvisor.sqllite')

    # Create all tables if they don't exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    user = (session.query(User)
            .filter_by(user_username='thartman').first())
    print(user)
    roles = user.roles
    print(roles)
    user.user_email = 'junk@nowhere.com'
    session.commit()
