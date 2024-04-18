from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Estado_alerta(Base_table):
#     __tablename__ = 'estado_alerta'
    
#     id_estado_alerta = Column(Integer, primary_key=True, name="id_estado_alerta")
#     nombre = Column(String(50), nullable=False, name="nombre")

class Estado_alertaDTO(BaseModel):
    id_estado_alerta: Optional[int] = None
    nombre: str
    
class Create_estado_alertaDTO(BaseModel):
    nombre: str

class Update_estado_alertaDTO(BaseModel):
    nombre: Optional[str] = None