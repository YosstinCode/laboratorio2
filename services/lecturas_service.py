from models.Lecturas import Lecturas
from services.CRUD import CRUD

class LecturasService(CRUD):
    
    def __init__(self):        
        super().__init__(Lecturas)