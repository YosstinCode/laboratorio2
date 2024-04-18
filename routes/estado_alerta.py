from fastapi import APIRouter

from services.estado_alerta_service import Estado_alerta_service
from schemas.Estado_alertaDTO import Create_estado_alertaDTO, Update_estado_alertaDTO

estado_alerta_router = APIRouter()
estado_alerta_service = Estado_alerta_service()

@estado_alerta_router.get("/")
async def get_all_estado_alerta():
    return estado_alerta_service.get_all()


@estado_alerta_router.post("/")
async def create_estado_alerta_route(estado_alerta: Create_estado_alertaDTO):
    return estado_alerta_service.create(estado_alerta)


@estado_alerta_router.get("/{estado_alerta_id}")
async def get_one_estado_alertas(estado_alerta_id: int):
    return estado_alerta_service.get_one(estado_alerta_id)


@estado_alerta_router.put("/{estado_alerta_id}")
async def update_estado_alerta_route(estado_alerta_id: int, estado_alerta_updated: Update_estado_alertaDTO):
    return estado_alerta_service.update(estado_alerta_id, estado_alerta_updated)


@estado_alerta_router.delete("/{estado_alerta_id}")
async def delete_estado_alerta_route(estado_alerta_id: int):
    return estado_alerta_service.delete(estado_alerta_id)