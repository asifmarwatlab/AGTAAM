from fastapi import APIRouter, Response, status

from app.shared.schemas import Message

from .. import service
from ..schemas import AnnotationCreate, DisplayToggles

router = APIRouter(prefix="/display", tags=["View · Display"])


@router.get("")
def get_display():
    return service.get_display()


@router.put("")
def update_display(req: DisplayToggles):
    """Switch Regions / Reference Grid / Annotation on or off."""
    return service.update_display(req.model_dump(exclude_none=True))


@router.get("/hillshade/{layer_id}", response_class=Response)
def hillshade(layer_id: str, azimuth: float = 315, altitude: float = 45, z_factor: float = 1.0):
    return Response(service.hillshade_image(layer_id, azimuth, altitude, z_factor), media_type="image/png")


@router.get("/slope/{layer_id}", response_class=Response)
def slope(layer_id: str, ramp: str = "slope"):
    return Response(service.slope_image(layer_id, ramp), media_type="image/png")


@router.get("/contours/{layer_id}")
def contours(layer_id: str, interval: float = 100.0, base: float = 0.0):
    return service.contours(layer_id, interval, base)


@router.get("/reference-grid/{layer_id}")
def reference_grid(layer_id: str, spacing: float):
    return service.reference_grid(layer_id, spacing)


@router.post("/annotations", status_code=status.HTTP_201_CREATED)
def add_annotation(req: AnnotationCreate):
    return service.add_annotation(req.x, req.y, req.text)


@router.delete("/annotations/{note_id}", response_model=Message)
def remove_annotation(note_id: str):
    service.remove_annotation(note_id)
    return Message(message="Annotation removed.")
