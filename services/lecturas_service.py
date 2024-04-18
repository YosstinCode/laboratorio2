from models.Lecturas import Lecturas
from services.CRUD import CRUD

class Lecturas_service(CRUD):
    
    def __init__(self):        
        super().__init__(Lecturas)