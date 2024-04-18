from sqlalchemy import Column, Integer, String
from config.database import Base_table

class Estados_huevos(Base_table):
    __tablename__ = 'estados_huevos'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_estado_huevo")
    nombre = Column(String(100), nullable=False, name="nombre")