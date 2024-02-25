from sqlalchemy import create_engine, Column, Integer, String, text
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

class Users_has_Dinosaurs(Base):
    __tablename__ = 'Users_has_Dinosaurs'
    Users_user_id = Column(Integer, primary_key=True)
    Dinosaurs_dino_id = Column(Integer,primary_key=True)


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
    
# function to retrieve dinosaurs that the user has in their inventory
def get_dinosaurs_ids(email):
    session = Session()
    user = session.query(Users).filter_by(user_email=email).first()

    # if the user exists
    if user:
        conn = engine.connect()
        # execute SQL
        query = text('SELECT Dinosaurs_dino_id FROM Users_has_Dinosaurs WHERE Users_user_id = :user_id')
        result = conn.execute(query,{'user_id': user.user_id })


        # Fetch all rows from the result
        dinosaurs = result.fetchall()
        conn.close()

        # take dinosaur IDs from the result
        dinosaur_ids = [row[0] for row in dinosaurs]

        return dinosaur_ids
    else:
        return []  # Return an empty list if user is not found or email is invalid

def get_dinosaurs_info(ids):
    with engine.connect() as conn:
        dinosaurs = []
        query = text("SELECT dino_breed, dino_image FROM Dinosaurs WHERE dino_id = :dino_id")
        for dino_id in ids:
            result = conn.execute(query, {'dino_id': dino_id})
            dinosaur_info = result.fetchone()
            if dinosaur_info:
                dinosaurs.append(dinosaur_info)

        return dinosaurs
    

def image_to_blob(image_path):
    with open(image_path, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(dino_id, blob_data):
    with engine.connect() as conn:
        query = text("UPDATE Dinosaurs SET dino_image = :blob_data WHERE dino_id = :dino_id")
        conn.execute(query, {'blob_data': blob_data, 'dino_id': dino_id})