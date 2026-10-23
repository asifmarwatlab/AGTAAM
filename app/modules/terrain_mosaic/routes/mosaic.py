from fastapi import APIRouter, Response

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import BlendSettings

router = APIRouter(prefix="/mosaic", tags=["Terrain Mosaic · Mosaic"])


@router.get("/blend-settings")
def get_blend_settings():
    return service.get_blend()


@router.put("/blend-settings")
def set_blend_settings(req: BlendSettings):
    return service.set_blend(req.method, req.feather_pixels)


@router.post("/preview")
def preview_mosaic(response: Response, background: bool = False):
    """background=true returns a job_id (poll /api/v1/jobs/{id}) instead of waiting."""
    result = service.preview(background)
    if background:
        response.status_code = 202
    return result


@router.post("/apply", response_model=DerivedLayerResult)
def apply_mosaic():
    return service.apply()
