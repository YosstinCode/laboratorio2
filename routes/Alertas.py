from fastapi import APIRouter

from services.Alertas_service import Alertas_service
from schemas.AlertasDTO import Create_alertasDTO, Update_alertasDTO

alertas_router = APIRouter()
alertas_service = Alertas_service()

@alertas_router.get("/")
async def get_all_alertas():
    return alertas_service.get_all()


@alertas_router.post("/")
async def create_alertas_route(alertas: Create_alertasDTO):
    return alertas_service.create(alertas)


@alertas_router.get("/{alertas_id}")
async def get_one_alertass(alertas_id: int):
    return alertas_service.get_one(alertas_id)


@alertas_router.put("/{alertas_id}")
async def update_alertas_route(alertas_id: int, alertas_updated: Update_alertasDTO):
    return alertas_service.update(alertas_id, alertas_updated)


@alertas_router.delete("/{alertas_id}")
async def delete_alertas_route(alertas_id: int):
    return alertas_service.delete(alertas_id)