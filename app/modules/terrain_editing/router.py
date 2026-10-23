from fastapi import APIRouter

from .routes import modify_terrain, output, review, selection

router = APIRouter(prefix="/terrain-editing")
for group in (selection, modify_terrain, review, output):
    router.include_router(group.router)
