from models.Huevos import Huevos
from services.CRUD import CRUD

class Huevos_service(CRUD):
    
    def __init__(self):        
        super().__init__(Huevos)
