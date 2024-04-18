from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import Base_table

class Huevos(Base_table):
    __tablename__ = 'huevos'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_huevo")
    columna = Column(Integer, nullable=False, name="columna")
    fila = Column(Integer, nullable=False, name="fila")
    fecha_hora_puesta = Column(DateTime, nullable=False, name="fecha_hora_puesta")
    fecha_hora_ingreso = Column(DateTime, nullable=False, name="fecha_hora_ingreso")
    fecha_hora_salida = Column(DateTime, nullable=False, name="fecha_hora_salida")
    dispositivo_id = Column(Integer, ForeignKey('dispositivos.id_dispositivo'), nullable=False, name="dispositivo_id")
    dispositivo = relationship("Dispositivos", backref="huevos", lazy=True)
    tipo_ave_id = Column(Integer, ForeignKey('tipo_ave.id_tipo_ave'), nullable=False, name="tipo_ave_id")
    tipo_ave = relationship("Tipo_ave", backref="huevos", lazy=True)
    
