# Importing necessary modules for database operations
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Setting up the DATABASE_URI from environment variable
DATABASE_URI = os.environ['DATABASE_URI']

# Creating an engine for the database connection
engine = create_engine(DATABASE_URI, echo=True)

# Configuring session for database operations
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Base class for declarative class definitions
Base = declarative_base()
Base.query = db_session.query_property()

# Defining the Job model with its respective fields
class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    location = Column(String(250))
    salary = Column(Numeric(10, 2))
    currency = Column(String(10))
    responsibilities = Column(String(2000))
    requirements = Column(String(2000))

# Defining the JobApplicant model with its respective fields
class JobApplicant(Base):
    __tablename__ = 'job_applicants'

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, nullable=False)
    job_title = Column(String(250))
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    birthday = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    linkedin = Column(String(250))
    education = Column(String(2000), nullable=False)
    experience = Column(String(2000), nullable=False)
    resume = Column(String)
    gender = Column(String(250), nullable=False)
    nationality = Column(String(250), nullable=False)
    status = Column(String(100), nullable=False, default='pending')
    username = Column(String(250), unique=True)
    password = Column(String(250))
    is_deleted = Column(Integer, default=0)

# Function to initialize the database with the defined models
def init_db():
    Base.metadata.create_all(bind=engine)