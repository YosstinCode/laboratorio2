from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
DATABASE = os.environ.get('DATABASE')

print(USER, PASSWORD, HOST, DATABASE)

# Database connection
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}')

# sesion para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Clase base para las tablas como una plantilla
Base_table = declarative_base(metadata=MetaData()) 
