import os
from dotenv import load_dotenv
load_dotenv()
# Reads credentials from the config file
user = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host = os.getenv('DATABASE_HOST')
dbname = os.getenv('DATABASE')

db_connection_string = f"mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4"

