from typing import Optional, List
from pydantic import BaseModel

# from sqlalchemy import Column, Integer, String, ForeignKey, Text
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Tipo_ave(Base_table):
#     __tablename__ = 'tipo_ave'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_ave")
#     imagen = Column(String(100), nullable=False, name="imagen")
#     nombre = Column(String(100), nullable=False, name="nombre")
#     descripcion = Column(Text, nullable=False, name="descripcion")
#     caracteristicas_incubacion_id = Column(Integer, ForeignKey('caracteristicas_incubacion.id_caracteristicas_incubacion'), nullable=False, name="caracteristicas_incubacion_id")
#     caracteristicas_incubacion = relationship("Caracteristicas_incubacion", backref="tipo_ave", lazy=True)

class Tipo_aveDTO(BaseModel):
    id_tipo_ave: Optional[int] = None
    imagen: str
    nombre: str
    descripcion: str
    caracteristicas_incubacion_id: int

class Create_tipo_aveDTO(BaseModel):
    imagen: str
    nombre: str
    descripcion: str
    caracteristicas_incubacion_id: int

class Update_tipo_aveDTO(BaseModel):
    imagen: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    caracteristicas_incubacion_id: Optional[int] = None