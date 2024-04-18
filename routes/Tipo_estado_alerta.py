from fastapi import APIRouter
from services.tipo_estado_alerta_service import Tipo_estado_alerta_service
from schemas.Tipo_estado_alertaDTO import Create_tipo_estado_alertaDTO, Update_tipo_estado_alertaDTO

tipo_estado_alerta_router = APIRouter()
tipo_estado_alerta_service = Tipo_estado_alerta_service()

@tipo_estado_alerta_router.get("/")
async def get_all_tipo_estado_alerta():
    return tipo_estado_alerta_service.get_all()

@tipo_estado_alerta_router.get("/{tipo_estado_alerta_id}")
async def get_one_tipo_estado_alerta(tipo_estado_alerta_id: int):
    return tipo_estado_alerta_service.get_one(tipo_estado_alerta_id)

@tipo_estado_alerta_router.post("/")
async def create_tipo_estado_alerta(tipo_estado_alerta: Create_tipo_estado_alertaDTO):
    return tipo_estado_alerta_service.create(tipo_estado_alerta)

@tipo_estado_alerta_router.put("/{tipo_estado_alerta_id}")
async def update_tipo_estado_alerta(tipo_estado_alerta_id: int, tipo_estado_alerta: Update_tipo_estado_alertaDTO):
    return tipo_estado_alerta_service.update(tipo_estado_alerta_id, tipo_estado_alerta)

@tipo_estado_alerta_router.delete("/{tipo_estado_alerta_id}")
async def delete_tipo_estado_alerta(tipo_estado_alerta_id: int):
    return tipo_estado_alerta_service.delete(tipo_estado_alerta_id)