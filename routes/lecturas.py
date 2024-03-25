from fastapi import APIRouter
from services.lecturas_service import LecturasService
from schemas.LecturaDTO import CreateLecturaDTO, UpdateLecturaDTO

lecturas_router = APIRouter()
lecturas_service = LecturasService()

@lecturas_router.get("/")
async def get_all_lecturas():
    return lecturas_service.get_all()

@lecturas_router.get("/{lectura_id}")
async def get_one_lectura(lectura_id: int):
    return lecturas_service.get_one(lectura_id)

@lecturas_router.post("/")
async def create_lectura(lectura: CreateLecturaDTO):
    return lecturas_service.create(lectura)

@lecturas_router.put("/{lectura_id}")
async def update_lectura(lectura_id: int, lectura: UpdateLecturaDTO):
    return lecturas_service.update(lectura_id, lectura)

@lecturas_router.delete("/{lectura_id}")
async def delete_lectura(lectura_id: int):
    return lecturas_service.delete(lectura_id)