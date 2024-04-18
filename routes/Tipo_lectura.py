from fastapi import APIRouter
from services.Tipo_lectura_service import Tipo_lectura_service
from schemas.Tipo_lecturaDTO import Create_tipo_lecturaDTO, Update_tipo_lecturaDTO

tipo_lectura_router = APIRouter()
tipo_lectura_service = Tipo_lectura_service()

@tipo_lectura_router.get("/")
async def get_all_tipo_lectura():
    return tipo_lectura_service.get_all()

@tipo_lectura_router.get("/{tipo_lectura_id}")
async def get_one_tipo_lectura(tipo_lectura_id: int):
    return tipo_lectura_service.get_one(tipo_lectura_id)

@tipo_lectura_router.post("/")
async def create_tipo_lectura(tipo_lectura: Create_tipo_lecturaDTO):
    return tipo_lectura_service.create(tipo_lectura)

@tipo_lectura_router.put("/{tipo_lectura_id}")
async def update_tipo_lectura(tipo_lectura_id: int, tipo_lectura: Update_tipo_lecturaDTO):
    return tipo_lectura_service.update(tipo_lectura_id, tipo_lectura)

@tipo_lectura_router.delete("/{tipo_lectura_id}")
async def delete_tipo_lectura(tipo_lectura_id: int):
    return tipo_lectura_service.delete(tipo_lectura_id)