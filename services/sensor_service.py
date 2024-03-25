from services.CRUD import CRUD
from models.Sensores import Sensores

class SensorService(CRUD):
    
    def __init__(self):
        super().__init__(Sensores)