from fastapi import APIRouter

from .routes import input, mosaic, output, overlap_analysis

router = APIRouter(prefix="/terrain-mosaic")
for group in (input, overlap_analysis, mosaic, output):
    router.include_router(group.router)
