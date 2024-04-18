from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.database import Base_table

class Tipo_ave(Base_table):
    __tablename__ = 'tipo_ave'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_ave")
    imagen = Column(String(100), nullable=False, name="imagen")
    nombre = Column(String(100), nullable=False, name="nombre")
    descripcion = Column(Text, nullable=False, name="descripcion")
    caracteristicas_incubacion_id = Column(Integer, ForeignKey('caracteristicas_incubacion.id_caracteristicas_incubacion'), nullable=False, name="caracteristicas_incubacion_id")
    caracteristicas_incubacion = relationship("Caracteristicas_incubacion", backref="tipo_ave", lazy=True)
