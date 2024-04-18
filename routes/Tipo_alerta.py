from fastapi import APIRouter
from services.tipo_alerta_service import Tipo_alerta_service
from schemas.Tipo_alertaDTO import Create_tipo_alertaDTO, Update_tipo_alertaDTO

tipo_alerta_router = APIRouter()
tipo_alerta_service = Tipo_alerta_service()

@tipo_alerta_router.get("/")
async def get_all_tipo_alerta():
    return tipo_alerta_service.get_all()

@tipo_alerta_router.get("/{tipo_alerta_id}")
async def get_one_tipo_alerta(tipo_alerta_id: int):
    return tipo_alerta_service.get_one(tipo_alerta_id)

@tipo_alerta_router.post("/")
async def create_tipo_alerta(tipo_alerta: Create_tipo_alertaDTO):
    return tipo_alerta_service.create(tipo_alerta)

@tipo_alerta_router.put("/{tipo_alerta_id}")
async def update_tipo_alerta(tipo_alerta_id: int, tipo_alerta: Update_tipo_alertaDTO):
    return tipo_alerta_service.update(tipo_alerta_id, tipo_alerta)

@tipo_alerta_router.delete("/{tipo_alerta_id}")
async def delete_tipo_alerta(tipo_alerta_id: int):
    return tipo_alerta_service.delete(tipo_alerta_id)