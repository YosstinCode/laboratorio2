from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base_table

class Dispositivos(Base_table):
    __tablename__ = 'dispositivos'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_dispositivo")
    W = Column(String(20), nullable=False, name="W")
    N = Column(String(20), nullable=False, name="N")
    sensores = relationship("Sensores", backref="dispositivos", lazy=True)