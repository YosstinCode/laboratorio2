from models.Revision_huevos import Revision_huevos
from services.CRUD import CRUD

class Revision_huevos_service(CRUD):
    
    def __init__(self):        
        super().__init__(Revision_huevos)