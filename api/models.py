from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import secrets
# from sqlalchemy import Column, Integer, String
# from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.


class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    api_id = db.Column(db.String(16), default=secrets.token_hex(16))
    api_tocken = db.Column(db.String(16), default=secrets.token_hex(16))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

class Clients(Base):
    __tablename__ = 'Clients'

    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(24), default=secrets.token_hex())


# Create tables.
Base.metadata.create_all(bind=engine)
