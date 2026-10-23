from fastapi import APIRouter

from .. import service
from ..schemas import AreaRequest, DistanceRequest, ProfileRequest

router = APIRouter(prefix="/measure", tags=["Analysis · Measure"])


@router.post("/distance")
def distance(req: DistanceRequest):
    """Length of a line, in metres (haversine for lat/lon layers)."""
    return service.distance(req.layer_id, req.points)


@router.post("/area")
def area(req: AreaRequest):
    return service.area(req.layer_id, req.polygon)


@router.post("/elevation-profile")
def elevation_profile(req: ProfileRequest):
    return service.elevation_profile(req.layer_id, req.line, req.samples)
