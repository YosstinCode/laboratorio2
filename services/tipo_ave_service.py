from models.Tipo_ave import Tipo_ave
from services.CRUD import CRUD

class Tipo_ave_service(CRUD):
    
    def __init__(self):        
        super().__init__(Tipo_ave)