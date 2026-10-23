from fastapi import APIRouter

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import PairRequest

router = APIRouter(prefix="/overlap-analysis", tags=["Terrain Mosaic · Overlap Analysis"])


@router.post("/difference-map", response_model=DerivedLayerResult)
def difference_map(req: PairRequest | None = None):
    req = req or PairRequest()
    return service.make_difference_map(req.layer_a, req.layer_b)


@router.post("/seamline", response_model=DerivedLayerResult)
def create_seamline(req: PairRequest | None = None):
    req = req or PairRequest()
    return service.make_seamline(req.layer_a, req.layer_b)
