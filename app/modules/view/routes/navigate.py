from fastapi import APIRouter

from .. import service
from ..schemas import ModeRequest, ViewportUpdate, ZoomRequest

router = APIRouter(prefix="/navigate", tags=["View · Navigate"])


@router.post("/explore")
def explore(req: ModeRequest | None = None):
    """Switch the pointer tool (default: explore / pan)."""
    return service.set_mode(req.mode if req else "explore")


@router.get("/full-extent")
def full_extent():
    return service.full_extent()


@router.post("/zoom-in")
def zoom_in(req: ZoomRequest | None = None):
    return service.zoom((req or ZoomRequest()).factor, "in")


@router.post("/zoom-out")
def zoom_out(req: ZoomRequest | None = None):
    return service.zoom((req or ZoomRequest()).factor, "out")


@router.get("/zoom-to-layer/{layer_id}")
def zoom_to_layer(layer_id: str):
    return service.zoom_to_layer(layer_id)


@router.put("/viewport")
def update_viewport(req: ViewportUpdate):
    """The UI reports its centre/scale so zoom-in/out can stay in step."""
    return service.update_viewport(req.center, req.scale)
