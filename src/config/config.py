import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  SECRET_KEY = os.getenv("SECRET_KEY","dev")
  
  DB_USER = os.getenv("DB_USER", "root")
  DB_PASSWORD = os.getenv("DB_PASSWORD", "")
  DB_HOST = os.getenv("DB_HOST", "localhost")
  DB_NAME = os.getenv("DB_NAME", "flask_crud_2")
  SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"