from typing import Optional, List
from pydantic import BaseModel

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Tipo_alerta(Base_table):
#     __tablename__ = 'tipo_alerta'
    
#     id_tipo_alerta = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_alerta")
#     nombre = Column(String(50), nullable=False, name="nombre")

class Tipo_alertaDTO(BaseModel):
    id_tipo_alerta: Optional[int] = None
    nombre: str

class Create_tipo_alertaDTO(BaseModel):
    nombre: str

class Update_tipo_alertaDTO(BaseModel):
    nombre: Optional[str] = None