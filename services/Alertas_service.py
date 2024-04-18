from models.Alertas import Alertas
from services.CRUD import CRUD

class Alertas_service(CRUD):
    
    def __init__(self):        
        super().__init__(Alertas)
