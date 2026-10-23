from fastapi import APIRouter

from .. import service
from ..schemas import OptionsUpdate

router = APIRouter(prefix="/workspace", tags=["Tools · Workspace"])


@router.get("/options")
def get_options():
    return service.get_options()


@router.put("/options")
def update_options(req: OptionsUpdate):
    return service.update_options(req.model_dump(exclude_none=True))


@router.get("/shortcuts")
def shortcuts():
    return service.shortcuts()


@router.get("/about")
def about():
    return service.about()
