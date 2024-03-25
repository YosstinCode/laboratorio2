from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base_table

class Sensores(Base_table):
    __tablename__ = 'sensores'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_sensor")
    referencia = Column(String(20), nullable=False, name="referencia")
    descripcion = Column(Text, nullable=False, name="descripcion")
    dispositivo_id = Column(Integer, ForeignKey('dispositivos.id_dispositivo'), nullable=False, name="dispositivo_id")
    dispositivo = relationship("Dispositivos", back_populates="sensores") 
    lecturas = relationship("Lecturas", back_populates="sensor")
    