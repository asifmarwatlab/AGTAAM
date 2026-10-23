"""Front door of the API.

Every folder inside app/modules/ that has a router.py is mounted automatically,
so adding a new tab never requires editing this file. A module that fails to load is
logged and skipped - it cannot take the rest of the app down.
"""
from __future__ import annotations

import importlib
import logging
import pkgutil
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import modules
from app.shared.config import get_settings
from app.shared.errors import register_error_handlers
from app.shared.jobs import jobs
from app.shared.logging import setup_logging

log = logging.getLogger("terrain")


def mount_modules(app: FastAPI, prefix: str) -> list[str]:
    mounted: list[str] = []
    for info in pkgutil.iter_modules(modules.__path__):
        if not info.ispkg:
            continue
        try:
            mod = importlib.import_module(f"app.modules.{info.name}.router")
            app.include_router(mod.router, prefix=prefix)
            mounted.append(info.name)
        except Exception:                                   # noqa: BLE001
            log.exception("Module '%s' failed to load and was skipped", info.name)
    return mounted


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        settings.ensure_dirs()
        log.info("%s %s ready - modules: %s", settings.app_name, settings.app_version,
                 ", ".join(app.state.modules))
        yield

    app = FastAPI(title=settings.app_name, version=settings.app_version, debug=settings.debug,
                  lifespan=lifespan)
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins,
                       allow_methods=["*"], allow_headers=["*"])
    register_error_handlers(app)
    app.state.modules = mount_modules(app, settings.api_prefix)

    @app.get("/health", tags=["System"])
    def health():
        return {"status": "ok", "version": settings.app_version, "modules": app.state.modules}

    @app.get(f"{settings.api_prefix}/jobs", tags=["System"])
    def list_jobs():
        return [j.to_dict() for j in jobs.list()]

    @app.get(f"{settings.api_prefix}/jobs/{{job_id}}", tags=["System"])
    def get_job(job_id: str):
        return jobs.get(job_id).to_dict()

    return app


app = create_app()
