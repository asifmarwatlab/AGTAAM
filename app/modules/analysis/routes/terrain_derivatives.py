from fastapi import APIRouter

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import ContoursRequest, LayerRequest

router = APIRouter(prefix="/terrain-derivatives", tags=["Analysis · Terrain Derivatives"])


@router.post("/contours", response_model=DerivedLayerResult)
def contours(req: ContoursRequest):
    """Adds a vector layer; fetch its lines from /file/add-data/layers/{id}/geojson."""
    return service.contours(req.layer_id, req.interval, req.base)


@router.post("/roughness", response_model=DerivedLayerResult)
def roughness(req: LayerRequest):
    return service.roughness(req.layer_id)


@router.post("/tpi", response_model=DerivedLayerResult)
def tpi(req: LayerRequest):
    return service.tpi(req.layer_id)


@router.post("/ruggedness", response_model=DerivedLayerResult)
def ruggedness(req: LayerRequest):
    return service.ruggedness(req.layer_id)
