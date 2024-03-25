from typing import Optional, List
from pydantic import BaseModel

class SensorDTO(BaseModel):
    id: Optional[int]
    referencia: str
    descripcion: str
    dispositivo_id: int
    
