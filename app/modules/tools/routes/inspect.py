from fastapi import APIRouter

from .. import service
from ..schemas import IdentifyRequest

router = APIRouter(prefix="/inspect", tags=["Tools · Inspect"])


@router.post("/identify")
def identify(req: IdentifyRequest):
    """Click on the map: value, row/column and pixel centre at that point."""
    return service.identify(req.layer_id, req.x, req.y)


@router.get("/pixel/{layer_id}")
def pixel_inspector(layer_id: str, x: float, y: float):
    """Same as identify but as a GET, for the live Pixel Inspector as the mouse moves."""
    return service.identify(layer_id, x, y)


@router.get("/properties/{layer_id}")
def properties(layer_id: str):
    return service.properties(layer_id)


@router.get("/metadata/{layer_id}")
def metadata(layer_id: str):
    return service.metadata(layer_id)
