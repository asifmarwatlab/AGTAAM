from fastapi import APIRouter

from .routes import add_data, export, project, workspace

router = APIRouter(prefix="/file")
for group in (project, add_data, export, workspace):
    router.include_router(group.router)
