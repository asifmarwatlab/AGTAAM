from fastapi import APIRouter

from .. import service
from ..schemas import LayerRequest

router = APIRouter(prefix="/review", tags=["Terrain Editing · Review"])


@router.get("/pending/{layer_id}")
def pending(layer_id: str):
    return service.pending(layer_id)


@router.post("/preview")
def preview(req: LayerRequest):
    return service.preview(req.layer_id)


@router.post("/compare")
def compare(req: LayerRequest):
    return service.compare(req.layer_id)


@router.post("/discard")
def discard(req: LayerRequest):
    return service.discard(req.layer_id)
