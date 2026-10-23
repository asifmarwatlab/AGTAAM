from fastapi import APIRouter

from .. import service
from ..schemas import OpenResult, ProjectInfo, ProjectNew, ProjectPath, ProjectSave, SaveResult

router = APIRouter(prefix="/project", tags=["File · Project"])


@router.get("", response_model=ProjectInfo)
def current_project():
    """Name, path and unsaved-changes flag of the open project."""
    return service.project_info()


@router.post("/new", response_model=ProjectInfo)
def new_project(req: ProjectNew):
    return service.new_project(req.name)


@router.post("/open", response_model=OpenResult)
def open_project(req: ProjectPath):
    return service.open_project(req.path)


@router.post("/save", response_model=SaveResult)
def save_project(req: ProjectSave | None = None):
    return service.save_project(req.path if req else None)


@router.post("/save-as", response_model=SaveResult)
def save_project_as(req: ProjectPath):
    return service.save_project(req.path)
