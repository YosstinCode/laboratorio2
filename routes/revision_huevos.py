from fastapi import APIRouter
from services.revision_huevos_service import Revision_huevos_service
from schemas.Revision_huevosDTO import Create_revision_huevosDTO, Update_revision_huevosDTO

revision_huevos_router = APIRouter()
revision_huevos_service = Revision_huevos_service()

@revision_huevos_router.get("/")
async def get_all_revision_huevos():
    return revision_huevos_service.get_all()

@revision_huevos_router.get("/{revision_huevos_id}")
async def get_one_revision_huevos(revision_huevos_id: int):
    return revision_huevos_service.get_one(revision_huevos_id)

@revision_huevos_router.post("/")
async def create_revision_huevos(revision_huevos: Create_revision_huevosDTO):
    return revision_huevos_service.create(revision_huevos)

@revision_huevos_router.put("/{revision_huevos_id}")
async def update_revision_huevos(revision_huevos_id: int, revision_huevos: Update_revision_huevosDTO):
    return revision_huevos_service.update(revision_huevos_id, revision_huevos)

@revision_huevos_router.delete("/{revision_huevos_id}")
async def delete_revision_huevos(revision_huevos_id: int):
    return revision_huevos_service.delete(revision_huevos_id)