# Adding a feature without disturbing anything

## A. New button in an existing group (e.g. "Relief" in Terrain Derivatives)

1. Maths: `app/core/terrain/relief.py` with `compute_relief(dem) -> np.ndarray`.
2. Service: add `relief()` to `app/modules/analysis/service.py`
   (copy `roughness()`: get layer, call core, `_derive(...)`).
3. Endpoint: add 3 lines to `app/modules/analysis/routes/terrain_derivatives.py`.
4. Test: `tests/core/test_terrain.py` (known answer) and add the path to the parametrised
   list in `tests/modules/test_analysis_tools.py`.

Existing endpoints are not touched.

## B. New group in an existing tab

1. Create `app/modules/<tab>/routes/<group>.py` with `router = APIRouter(prefix="/<group>", tags=[...])`.
2. Add it to the tuple in that module's `router.py` (one line).

## C. New tab (e.g. Hydrology)

1. Create `app/modules/hydrology/` with `__init__.py`, `router.py`, `schemas.py`,
   `service.py`, `routes/__init__.py`, `routes/<group>.py`. Copy any small module as a template.
2. Nothing else. `main.py` finds it automatically. If it has a bug, it is logged and skipped;
   the other modules keep working.

## D. A breaking change to an existing endpoint

Do not edit it. Copy the module to `app/modules_v2/` (or add a `v2` router) and mount it at
`/api/v2`. Version 1 keeps working for the UI that still uses it.

## Rules that keep it clean

- Maths goes in `core/` and must run in a plain Python script (no FastAPI, no layer ids).
- A module never imports another module. Shared logic goes to `core/` or `shared/`.
- Buttons that appear on two tabs (Hillshade, Slope, Pixel Inspector) call the same `core`
  function from both modules; the maths exists once.
- Keep route functions to a few lines. If a route grows, the logic belongs in `service.py`.
