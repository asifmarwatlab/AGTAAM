from fastapi import APIRouter

from .routes import measure, quality_statistics, surface_analysis, terrain_derivatives

router = APIRouter(prefix="/analysis")
for group in (measure, quality_statistics, surface_analysis, terrain_derivatives):
    router.include_router(group.router)
