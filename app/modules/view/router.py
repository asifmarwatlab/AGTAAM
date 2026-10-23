from fastapi import APIRouter

from .routes import appearance, display, navigate, panes

router = APIRouter(prefix="/view")
for group in (navigate, panes, appearance, display):
    router.include_router(group.router)
