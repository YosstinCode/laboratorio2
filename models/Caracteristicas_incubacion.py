from sqlalchemy import Column, Integer
from config.database import Base_table

class Caracteristicas_incubacion(Base_table):
    __tablename__ = 'caracteristicas_incubacion'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, name="id_caracteristicas_incubacion")
    temperatura_minima = Column(Integer, nullable=False, name="temperatura_minima")
    temperatura_maxima = Column(Integer, nullable=False, name="temperatura_maxima")
    humedad_minima = Column(Integer, nullable=False, name="humedad_minima")
    humedad_maxima = Column(Integer, nullable=False, name="humedad_maxima")
    angulo_rotacion = Column(Integer, nullable=False, name="angulo_rotacion")
    tiempo_rotacion = Column(Integer, nullable=False, name="tiempo_rotacion")