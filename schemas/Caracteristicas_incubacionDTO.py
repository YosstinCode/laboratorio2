from pydantic import BaseModel
from typing import Optional, List


# from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship
# from config.database import Base_table

# class Caracteristicas_incubacion(Base_table):
#     __tablename__ = 'caracteristicas_incubacion'
    
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_caracteristicas_incubacion")
#     temp_minima = Column(Integer, nullable=False, name="temperatura_minima")
#     temp_maxima = Column(Integer, nullable=False, name="temperatura_maxima")
#     humedad_minima = Column(Integer, nullable=False, name="humedad_minima")
#     humedad_maxima = Column(Integer, nullable=False, name="humedad_maxima")
#     angulo_rotacion = Column(Integer, nullable=False, name="angulo_rotacion")
#     tiempo_rotacion = Column(Integer, nullable=False, name="tiempo_rotacion")

class Caracteristicas_incubacionDTO(BaseModel):
    id_caracteristicas_incubacion: Optional[int] = None
    temperatura_minima: int
    temperatura_maxima: int
    humedad_minima: int
    humedad_maxima: int
    angulo_rotacion: int
    tiempo_rotacion: int

class Create_caracteristicas_incubacionDTO(BaseModel):
    temperatura_minima: int
    temperatura_maxima: int
    humedad_minima: int
    humedad_maxima: int
    angulo_rotacion: int
    tiempo_rotacion: int

class Update_caracteristicas_incubacionDTO(BaseModel):
    temperatura_minima: Optional[int] = None
    temperatura_maxima: Optional[int] = None
    humedad_minima: Optional[int] = None
    humedad_maxima: Optional[int] = None
    angulo_rotacion: Optional[int] = None
    tiempo_rotacion: Optional[int] = None