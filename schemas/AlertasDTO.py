from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Alertas(Base_table):
#     __tablename__ = 'alertas'
    
#     fecha_alertas = Column(DateTime, nullable=False, name="fecha_alertas")
#     lectura_id = Column(Integer, ForeignKey('lecturas.id_lectura'), nullable=False, name="lectura_id")
#     lectura = relationship("Lecturas", backref="alertas", lazy=True)
#     tipo_estado_alerta_id = Column(Integer, ForeignKey('tipo_estado_alerta.id_tipo_estado_alerta'), nullable=False, name="tipo_estado_alerta_id")
#     tipo_estado_alerta = relationship("Tipo_estado_alerta", backref="alertas", lazy=True)

class AlertasDTO(BaseModel):
    id_alerta: Optional[int] = None
    fecha_alerta: str
    lectura_id: int
    tipo_estado_alerta_id: int

class Create_alertasDTO(BaseModel):
    fecha_alerta: str
    lectura_id: int
    tipo_estado_alerta_id: int
    
class Update_alertasDTO(BaseModel):
    fecha_alerta: Optional[str] = None
    lectura_id: Optional[int] = None
    tipo_estado_alerta_id: Optional[int] = None