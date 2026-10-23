from fastapi import APIRouter

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import HillshadeRequest, LayerRequest, SlopeRequest

router = APIRouter(prefix="/surface-analysis", tags=["Analysis · Surface Analysis"])


@router.post("/hillshade", response_model=DerivedLayerResult)
def hillshade(req: HillshadeRequest):
    return service.hillshade(req.layer_id, req.azimuth, req.altitude, req.z_factor)


@router.post("/slope", response_model=DerivedLayerResult)
def slope(req: SlopeRequest):
    return service.slope(req.layer_id, req.units)


@router.post("/aspect", response_model=DerivedLayerResult)
def aspect(req: LayerRequest):
    return service.aspect(req.layer_id)


@router.post("/curvature", response_model=DerivedLayerResult)
def curvature(req: LayerRequest):
    return service.curvature(req.layer_id)
