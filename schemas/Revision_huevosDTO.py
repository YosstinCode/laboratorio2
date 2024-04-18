from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Revision_huevos(Base_table):
#     __tablename__ = 'revision_huevos'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_revision_huevos")
#     fecha_revision = Column(DateTime, nullable=False, name="fecha_revision")
#     observacion = Column(Text, nullable=False, name="observacion")
#     estado_huevo_id = Column(Integer, ForeignKey('estado_huevo.id_estado_huevo'), nullable=False, name="estado_huevo_id")
#     estado_huevo = relationship("Estado_huevo", backref="revision_huevos", lazy=True)
#     id_huevo = Column(Integer, ForeignKey('huevos.id_huevo'), nullable=False, name="id_huevo")
#     huevo = relationship("Huevos", backref="revision_huevos", lazy=True)

class Revision_huevosDTO(BaseModel):
    id_revision_huevos: Optional[int] = None
    fecha_revision: str
    observacion: str
    estado_huevo_id: int
    id_huevo: int

class Create_revision_huevosDTO(BaseModel):
    fecha_revision: str
    observacion: str
    estado_huevo_id: int
    id_huevo: int
    
class Update_revision_huevosDTO(BaseModel):
    fecha_revision: Optional[str] = None
    observacion: Optional[str] = None
    estado_huevo_id: Optional[int] = None
    id_huevo: Optional[int] = None