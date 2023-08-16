import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post  # Import your models

fake = Faker()

def generate_users(session, count=10):
    for _ in range(count):
        user = User(
            username=fake.user_name(),
            email=fake.email()
        )
        session.add(user)

def generate_posts(session, users, count=20):
    for _ in range(count):
        post = Post(
            title=fake.sentence(),
            content=fake.paragraph(),
            author=random.choice(users)
        )
        session.add(post)

# Create a session
engine = create_engine('sqlite:///mytestdb.db')
Session = sessionmaker(bind=engine)
session = Session()

# Generate users and posts
generate_users(session)
users = session.query(User).all()
generate_posts(session, users)

# Commit changes and close the session
session.commit()
session.close()