from typing import Literal

from fastapi import APIRouter

from .. import service

router = APIRouter(prefix="/quality-statistics", tags=["Analysis · Quality & Statistics"])


@router.get("/layer-statistics/{layer_id}")
def layer_statistics(layer_id: str):
    return service.layer_statistics(layer_id)


@router.get("/histogram/{layer_id}")
def histogram(layer_id: str, bins: int = 50):
    return service.get_histogram(layer_id, bins)


@router.get("/nodata-check/{layer_id}")
def nodata_check(layer_id: str):
    return service.nodata(layer_id)


@router.get("/outlier-check/{layer_id}")
def outlier_check(layer_id: str, method: Literal["iqr", "zscore"] = "iqr",
                  threshold: float | None = None):
    return service.outlier_check(layer_id, method, threshold)
