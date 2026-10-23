from fastapi import APIRouter

from .routes import data_management, inspect, workspace

router = APIRouter(prefix="/tools")
for group in (data_management, inspect, workspace):
    router.include_router(group.router)
