from fastapi import APIRouter

from .. import service
from ..schemas import ExportMosaicRequest

router = APIRouter(prefix="/output", tags=["Terrain Mosaic · Output"])


@router.post("/export-elevations")
def export_elevations(req: ExportMosaicRequest):
    return service.export_elevations(req.path)
