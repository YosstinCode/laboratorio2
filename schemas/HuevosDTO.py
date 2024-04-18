from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Tipo_ave(Base_table):
#     __tablename__ = 'tipo_ave'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_tipo_ave")
#     columna = Column(Integer, nullable=False, name="columna")
#     fila = Column(Integer, nullable=False, name="fila")
#     fecha_hora_puesta = Column(DateTime, nullable=False, name="fecha_hora_puesta")
#     fecha_hora_ingreso = Column(DateTime, nullable=False, name="fecha_hora_ingreso")
#     fecha_hora_salida = Column(DateTime, nullable=False, name="fecha_hora_salida")
#     dispositivo_id = Column(Integer, ForeignKey('dispositivo.id_dispositivo'), nullable=False, name="dispositivo_id")
#     dispositivo = relationship("Dispositivo", backref="tipo_ave", lazy=True)
#     tipo_ave_id = Column(Integer, ForeignKey('tipo_ave.id_tipo_ave'), nullable=False, name="tipo_ave_id")
#     tipo_ave = relationship("Tipo_ave", backref="tipo_ave", lazy=True)
    

class HuevosDTO(BaseModel):
    id_huevo: Optional[int] = None
    columna: int
    fila: int
    fecha_hora_puesta: str
    fecha_hora_ingreso: str
    fecha_hora_salida: str
    dispositivo_id: int
    tipo_ave_id: int

class Create_huevosDTO(BaseModel):
    columna: int
    fila: int
    fecha_hora_puesta: str
    fecha_hora_ingreso: str
    fecha_hora_salida: str
    dispositivo_id: int
    tipo_ave_id: int

class Update_huevosDTO(BaseModel):
    columna: Optional[int] = None
    fila: Optional[int] = None
    fecha_hora_puesta: Optional[str] = None
    fecha_hora_ingreso: Optional[str] = None
    fecha_hora_salida: Optional[str] = None
    dispositivo_id: Optional[int] = None
    tipo_ave_id: Optional[int] = None