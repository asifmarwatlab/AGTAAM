from fastapi import APIRouter

from .. import service
from ..schemas import FullscreenRequest

router = APIRouter(prefix="/workspace", tags=["File · Workspace"])


@router.post("/reset")
def reset_workspace():
    """Panels, appearance and display settings back to defaults (layers stay)."""
    return service.reset_workspace()


@router.put("/fullscreen")
def fullscreen(req: FullscreenRequest):
    return service.set_fullscreen(req.enabled)


@router.post("/exit")
def exit_app():
    """Tells the UI whether there are unsaved changes before it closes."""
    return service.exit_info()
