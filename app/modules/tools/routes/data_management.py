from fastapi import APIRouter

from app.shared.schemas import DerivedLayerResult

from .. import service
from ..schemas import ClipRequest, FillNoDataRequest, ReprojectRequest, ResampleRequest

router = APIRouter(prefix="/data-management", tags=["Tools · Data Management"])


@router.post("/clip", response_model=DerivedLayerResult)
def clip(req: ClipRequest):
    return service.clip(req.layer_id, req.bounds.as_tuple())


@router.post("/resample", response_model=DerivedLayerResult)
def resample(req: ResampleRequest):
    return service.resample(req.layer_id, req.cell_size, req.method)


@router.post("/reproject", response_model=DerivedLayerResult)
def reproject(req: ReprojectRequest):
    return service.reproject(req.layer_id, req.epsg, req.method)


@router.post("/fill-nodata", response_model=DerivedLayerResult)
def fill_nodata(req: FillNoDataRequest):
    return service.fill_nodata(req.layer_id, req.max_iterations)
