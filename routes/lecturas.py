from fastapi import APIRouter
from services.lecturas_service import Lecturas_service
from schemas.LecturaDTO import Create_lecturaDTO, Update_lecturaDTO

lecturas_router = APIRouter()
lecturas_service = Lecturas_service()

@lecturas_router.get("/")
async def get_all_lecturas():
    return lecturas_service.get_all()

@lecturas_router.get("/{lectura_id}")
async def get_one_lectura(lectura_id: int):
    return lecturas_service.get_one(lectura_id)

@lecturas_router.post("/")
async def create_lectura(lectura: Create_lecturaDTO):
    return lecturas_service.create(lectura)

@lecturas_router.put("/{lectura_id}")
async def update_lectura(lectura_id: int, lectura: Update_lecturaDTO):
    return lecturas_service.update(lectura_id, lectura)

@lecturas_router.delete("/{lectura_id}")
async def delete_lectura(lectura_id: int):
    return lecturas_service.delete(lectura_id)