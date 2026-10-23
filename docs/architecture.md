# Architecture

Three layers, each with one job. Imports only go **downwards**.

```
modules/   ->  shared/  ->  core/
(web)          (state)      (maths)
```

| Layer | Job | Organised by | Knows FastAPI? |
|---|---|---|---|
| `app/modules/` | Receive the click, validate it, return JSON | The ribbon: tab = module, group = `routes/<group>.py` | Yes |
| `app/shared/` | Things every module needs: layer memory, project, jobs, errors, settings | Function | Partly (errors, schemas) |
| `app/core/` | The maths and file handling | The science: raster, terrain, stats, measure, editing, mosaic, render | **Never** |

Modules never import each other. `core` imports nothing from `shared` or `modules`.

## Inside a module

| File | Job |
|---|---|
| `router.py` | Joins the group files and sets the URL prefix (`/analysis`) |
| `schemas.py` | Request and response shapes (Pydantic) |
| `service.py` | Finds the layer, calls `core`, packages the answer. No web code |
| `routes/<group>.py` | One file per ribbon group. Endpoints stay a few lines long |

## One request, step by step

```
GET /api/v1/analysis/quality-statistics/histogram/ab12cd34?bins=50
  main.py                         mounts every module's router under /api/v1
  analysis/router.py              prefix /analysis
  routes/quality_statistics.py    prefix /quality-statistics -> histogram()
  service.get_histogram()         layer_store.get_raster_layer("ab12cd34")
  core/stats/histogram.py         numpy does the work
  <- JSON
```

## Layers and derived layers

`shared/layer_store.py` remembers every loaded layer by id. Tools that produce something
(slope, clip, mosaic...) add a **new** layer with `derived_from` and `tool` set; they never
overwrite the source. Derived layers live in memory until exported, so a saved project only
stores layers that have a file (`skipped_layers` in the save reply lists the rest).

## Errors

`core` raises plain `ValueError` / `FileNotFoundError`; `shared/errors.py` turns them into
`400` / `404` JSON (`{"error": "...", "message": "..."}`). Services raise `BadRequest`,
`NotFound`, `Conflict` for expected problems.

## Slow work

`shared/jobs.py` runs a function in a thread and tracks progress. Example in
`terrain_mosaic`: `POST /terrain-mosaic/mosaic/preview?background=true` returns `202` and a
`job_id`; poll `GET /api/v1/jobs/{job_id}`.

## Limits worth knowing

- One user / one project at a time (state is in memory). Fine for a local desktop app.
- Rasters are held fully in memory as float32 (a 3601x3601 tile is about 50 MB).
- Only north-up, single-band rasters. Rotated rasters are rejected with a clear message.
- Cell size in metres is estimated from latitude for lat/lon DEMs (fine for slope and hillshade).

## The client

`terrain_client/` is a separate package (needs only `httpx`) that mirrors the ribbon:
`api.<tab>.<button>()`. It never imports `app`. A contract test calls every client method
against the real backend and compares the result with `/openapi.json`, so the two cannot
drift apart silently.

## Session state follows the layers

Edit sessions and the mosaic selection refer to layer ids, so they register hooks on
`layer_store` (`on_remove`, `on_clear`) and are dropped when a layer is removed or the project
changes. Any new module that keeps per-layer state should do the same.
