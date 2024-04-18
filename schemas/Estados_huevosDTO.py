from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String, ForeignKey, Text
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Estados_huevos(Base_table):
#     __tablename__ = 'estados_huevos'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_estado_huevo")
#     nombre = Column(String(100), nullable=False, name="nombre")

class Estados_huevosDTO(BaseModel):
    id_estado_huevo: Optional[int] = None
    nombre: str

class Create_estados_huevosDTO(BaseModel):
    nombre: str

class Update_estados_huevosDTO(BaseModel):
    nombre: Optional[str] = None