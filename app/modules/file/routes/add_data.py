from fastapi import APIRouter, status

from app.shared.schemas import LayerInfo, Message

from .. import service
from ..schemas import (AddBasemapRequest, AddRasterRequest, AddVectorRequest, LayerOrder,
                       LayerUpdate)

router = APIRouter(prefix="/add-data", tags=["File · Add Data"])


@router.post("/raster", response_model=LayerInfo, status_code=status.HTTP_201_CREATED)
def add_raster(req: AddRasterRequest):
    return service.add_raster(req.path, req.name)


@router.post("/vector", response_model=LayerInfo, status_code=status.HTTP_201_CREATED)
def add_vector(req: AddVectorRequest):
    return service.add_vector(req.path, req.name)


@router.post("/basemap", response_model=LayerInfo, status_code=status.HTTP_201_CREATED)
def add_basemap(req: AddBasemapRequest):
    return service.add_basemap(req.name, req.url_template, req.attribution)


@router.get("/layers", response_model=list[LayerInfo])
def list_layers():
    """Layers in drawing order, top first (feeds the Layers panel)."""
    return service.list_layers()


@router.put("/layers/order", response_model=list[LayerInfo])
def reorder_layers(req: LayerOrder):
    return service.reorder_layers(req.layer_ids)


@router.patch("/layers/{layer_id}", response_model=LayerInfo)
def update_layer(layer_id: str, req: LayerUpdate):
    return service.update_layer(layer_id, req.model_dump(exclude_none=True))


@router.delete("/layers/{layer_id}", response_model=Message)
def remove_layer(layer_id: str):
    service.remove_layer(layer_id)
    return Message(message="Layer removed.")


@router.get("/layers/{layer_id}/geojson")
def layer_geojson(layer_id: str):
    return service.layer_geojson(layer_id)
