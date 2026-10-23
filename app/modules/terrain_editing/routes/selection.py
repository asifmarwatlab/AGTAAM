from fastapi import APIRouter, status

from .. import service
from ..schemas import LayerRequest, RegionCreate, RegionSelect

router = APIRouter(prefix="/selection", tags=["Terrain Editing · Selection"])


@router.post("/draw-region", status_code=status.HTTP_201_CREATED)
def draw_region(req: RegionCreate):
    return service.draw_region(req.layer_id, req.polygon, req.name)


@router.get("/regions/{layer_id}")
def list_regions(layer_id: str):
    return service.list_regions(layer_id)


@router.post("/select-region")
def select_region(req: RegionSelect):
    return service.select_regions(req.layer_id, req.region_ids)


@router.post("/delete-selected")
def delete_selected(req: LayerRequest):
    return service.delete_selected(req.layer_id)


@router.post("/clear-all")
def clear_all(req: LayerRequest):
    return service.clear_all(req.layer_id)
