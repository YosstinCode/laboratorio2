from pydantic import BaseModel
from typing import Optional, List

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Dispositivos(Base_table):
#     __tablename__ = 'dispositivos'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_dispositivo")
#     W = Column(String(20), nullable=False, name="W")
#     N = Column(String(20), nullable=False, name="N")
#     caracteristica_incubacion_id = Column(Integer, nullable=False, name="caracteristica_incubacion_id")
#     caracteristica_incubacion = relationship("Caracteristica_incubacion", backref="dispositivos", lazy=True)

class DispositivoDTO(BaseModel):
    id_dispositivo: Optional[int] = None
    W: str
    N: str
    caracteristica_incubacion_id: int

class Create_dispositivoDTO(BaseModel):
    W: str
    N: str
    caracteristica_incubacion_id: int

class Update_dispositivoDTO(BaseModel):
    W: Optional[str] = None
    N: Optional[str] = None
    caracteristica_incubacion_id: Optional[int] = None