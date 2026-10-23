from fastapi import APIRouter

from .. import service
from ..schemas import AppearanceUpdate

router = APIRouter(prefix="/appearance", tags=["View · Appearance"])


@router.get("")
def get_appearance():
    return service.get_appearance()


@router.put("")
def update_appearance(req: AppearanceUpdate):
    return service.update_appearance(req.model_dump(exclude_none=True))


@router.get("/colour-ramps")
def colour_ramps():
    return service.colour_ramps()
