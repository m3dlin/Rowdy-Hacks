from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
# Reads credentials from the config file
user = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host = os.getenv('DATABASE_HOST')
dbname = os.getenv('DATABASE')

db_connection_string = f"mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String)
    user_name = Column(String)

# function to check whether account exists or not
def check_credentials(email):
    # new database connection
    session = Session()
    # query on User table, and filtering the results by email.
    user = session.query(Users).filter_by(user_email=email).first() 

    # return the status of whether or not the user exists
    if user:
        session.close()
        return True
    else:
        session.close()
        return False