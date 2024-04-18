from typing import Optional, List
from pydantic import BaseModel

# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Sensores(Base_table):
#     __tablename__ = 'sensores'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_sensor")
#     referencia = Column(String(20), nullable=False, name="referencia")
#     descripcion = Column(Text, nullable=False, name="descripcion")
#     dispositivo_id = Column(Integer, ForeignKey('dispositivos.id_dispositivo'), nullable=False, name="dispositivo_id")
#     dispositivo = relationship("Dispositivos", backref="sensores", lazy=True)
    

class SensorDTO(BaseModel):
    id_sensor: Optional[int] = None
    referencia: str
    descripcion: str
    dispositivo_id: int

class Create_sensorDTO(BaseModel):
    referencia: str
    descripcion: str
    dispositivo_id: int

class Update_sensorDTO(BaseModel):
    referencia: Optional[str] = None
    descripcion: Optional[str] = None
    dispositivo_id: Optional[int] = None