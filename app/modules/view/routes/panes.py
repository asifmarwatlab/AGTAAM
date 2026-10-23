from fastapi import APIRouter

from .. import service
from ..schemas import PaneUpdate

router = APIRouter(prefix="/panes", tags=["View · Panes"])


@router.get("")
def get_panes():
    """Which panels are open: contents, statistics, pixel_inspector."""
    return service.get_panes()


@router.put("/{pane}")
def set_pane(pane: str, req: PaneUpdate):
    return service.set_pane(pane, req.visible)
