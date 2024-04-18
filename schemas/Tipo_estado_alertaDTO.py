from typing import Optional, List
from pydantic import BaseModel

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Tipo_estado_alerta(Base_table):
#     __tablename__ = 'tipo_alerta'
    
#     id_tipo_estado_alerta = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_alerta")
#     estado_alerta_id = Column(Integer, ForeignKey('estado_alerta.id_estado_alerta'), nullable=False, name="estado_alerta_id")
#     tipo_alerta_id = Column(Integer, ForeignKey('tipo_alerta.id_tipo_alerta'), nullable=False, name="tipo_alerta_id")
#     estado_alerta = relationship("Estado_alerta", backref="tipo_estado_alerta", lazy=True)
#     tipo_alerta = relationship("Tipo_alerta", backref="tipo_estado_alerta", lazy=True)

class Tipo_estado_alertaDTO(BaseModel):
    id_tipo_estado_alerta: Optional[int] = None
    estado_alerta_id: int
    tipo_alerta_id: int

class Create_tipo_estado_alertaDTO(BaseModel):
    estado_alerta_id: int
    tipo_alerta_id: int

class Update_tipo_estado_alertaDTO(BaseModel):
    estado_alerta_id: Optional[int] = None
    tipo_alerta_id: Optional[int] = None