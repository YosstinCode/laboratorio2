from pydantic import BaseModel
from typing import Optional, List

class LecturaDTO(BaseModel):
    id: Optional[int]
    fecha_hora: str
    valor: str
    sensor_id: int
    
class CreateLecturaDTO(BaseModel):
    fecha_hora: str
    valor: str
    sensor_id: int

class UpdateLecturaDTO(BaseModel):
    fecha_hora: Optional[str] = None
    valor: Optional[str] = None
    sensor_id: Optional[int] = None