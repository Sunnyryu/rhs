import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWD')
DB_NAME = os.getenv('DB')

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
