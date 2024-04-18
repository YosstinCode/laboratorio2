from services.CRUD import CRUD
from models.Sensores import Sensores

class Sensor_service(CRUD):
    
    def __init__(self):
        super().__init__(Sensores)