from fastapi import APIRouter

from services.dispositivo_service import DispositivoService
from schemas.DispositivoDTO import CreateDispositivoDTO, UpdateDispositivoDTO

dispositivos_router = APIRouter()
dispositivo_service = DispositivoService() 

@dispositivos_router.get("/")
async def get_all_dispositivos():
    return dispositivo_service.get_all()


@dispositivos_router.post("/")
async def create_dispositivo_route(dispositivo: CreateDispositivoDTO):
    return dispositivo_service.create(dispositivo)


@dispositivos_router.get("/{dispositivo_id}")
async def get_one_dispositivos(dispositivo_id: int):
    return dispositivo_service.get_one(dispositivo_id)


@dispositivos_router.put("/{dispositivo_id}")
async def update_dispositivo_route(dispositivo_id: int, dispositivo_updated: UpdateDispositivoDTO):
    return dispositivo_service.update(dispositivo_id, dispositivo_updated)


@dispositivos_router.delete("/{dispositivo_id}")
async def delete_dispositivo_route(dispositivo_id: int):
    return dispositivo_service.delete(dispositivo_id)
