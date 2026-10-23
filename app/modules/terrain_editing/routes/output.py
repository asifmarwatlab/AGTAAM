from fastapi import APIRouter

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import ExportEditedRequest, LayerRequest

router = APIRouter(prefix="/output", tags=["Terrain Editing · Output"])


@router.post("/apply", response_model=DerivedLayerResult)
def apply_edits(req: LayerRequest):
    """Creates a new '(edited)' layer. The original stays untouched."""
    return service.apply(req.layer_id)


@router.post("/export-edited-dem")
def export_edited_dem(req: ExportEditedRequest):
    return service.export_edited(req.layer_id, req.path)
