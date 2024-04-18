from typing import Optional, List
from pydantic import BaseModel

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Tipo_lectura(Base_table):
#     __tablename__ = 'tipo_lectura'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_lectura")
#     nombre = Column(String(100), nullable=False, name="nombre")

class Tipo_lecturaDTO(BaseModel):
    id_tipo_lectura: Optional[int] = None
    nombre: str
    
class Create_tipo_lecturaDTO(BaseModel):
    nombre: str

class Update_tipo_lecturaDTO(BaseModel):
    nombre: Optional[str] = None