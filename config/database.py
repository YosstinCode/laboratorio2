from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')

# Database connection
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}')

# Sesion para intereactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Clase base para las tablas como una plantilla
Base_table = declarative_base(metadata=MetaData()) 

# Crear las tablas en la DB
Base_table.metadata.create_all(engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

