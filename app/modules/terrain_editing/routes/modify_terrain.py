from fastapi import APIRouter

from .. import service
from ..schemas import FillSinksRequest, FlattenRequest, RaiseLowerRequest, SmoothRequest

router = APIRouter(prefix="/modify-terrain", tags=["Terrain Editing · Modify Terrain"])


@router.post("/raise-lower")
def raise_lower(req: RaiseLowerRequest):
    """Queues the edit. Nothing changes until Apply."""
    return service.queue(req.layer_id, "raise_lower", {"amount": req.amount}, req.region_ids)


@router.post("/smooth")
def smooth(req: SmoothRequest):
    return service.queue(req.layer_id, "smooth", {"iterations": req.iterations}, req.region_ids)


@router.post("/flatten")
def flatten(req: FlattenRequest):
    return service.queue(req.layer_id, "flatten", {"elevation": req.elevation}, req.region_ids)


@router.post("/fill-sinks")
def fill_sinks(req: FillSinksRequest):
    return service.queue(req.layer_id, "fill_sinks", {}, req.region_ids)
