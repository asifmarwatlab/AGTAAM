from typing import Literal

from fastapi import APIRouter, Query, Response

from .. import service
from ..schemas import ExportElevationsRequest

router = APIRouter(prefix="/export", tags=["File · Export"])


@router.get("/map-image/{layer_id}", response_class=Response)
def map_image(layer_id: str, ramp: str = "terrain", vmin: float | None = None,
              vmax: float | None = None, max_pixels: int | None = Query(None, gt=0)):
    """The layer drawn as a PNG."""
    return Response(service.map_image(layer_id, ramp, vmin, vmax, max_pixels), media_type="image/png")


@router.post("/elevations")
def export_elevations(req: ExportElevationsRequest):
    """Write the layer's elevations to a GeoTIFF."""
    return service.export_elevations(req.layer_id, req.path)


@router.get("/statistics/{layer_id}")
def export_statistics(layer_id: str, format: Literal["json", "csv"] = "json"):
    result = service.statistics(layer_id, format)
    if format == "csv":
        return Response(result, media_type="text/csv")
    return result
