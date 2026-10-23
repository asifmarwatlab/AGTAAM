from fastapi import APIRouter

from .. import service
from ..schemas import SelectDems

router = APIRouter(prefix="/input", tags=["Terrain Mosaic · Input"])


@router.post("/select-dems")
def select_dems(req: SelectDems):
    """Pick the DEM layers to merge. Reports whether they share a CRS and cell size."""
    return service.select_dems(req.layer_ids)


@router.get("/select-dems")
def get_selection():
    return service.get_selection()
