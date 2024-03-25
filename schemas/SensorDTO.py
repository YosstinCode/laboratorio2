from typing import Optional, List
from pydantic import BaseModel

class SensorDTO(BaseModel):
    id: Optional[int]
    referencia: str
    descripcion: str
    dispositivo_id: int
    
class CreateSensorDTO(BaseModel):
    referencia: str
    descripcion: str
    dispositivo_id: int
    
class UpdateSensorDTO(BaseModel):
    referencia: Optional[str] = None
    descripcion: Optional[str] = None
    dispositivo_id: Optional[int] = None