# AGENTS

## Project overview
- Prototype FastAPI app serving Jinja2-rendered HTML fragments for an HTMX-driven dashboard.
- Data is mocked in `backend/main.py` and injected into templates under `backend/templates/`.
- Static HTML mockups live at repo root (`htmx_index.html`, `original_index.html`) and are not served by the FastAPI app.

## Architecture & data flow
- FastAPI app entrypoint: `backend/main.py` (`app = FastAPI()`).
- HTMX pages request server-rendered fragments:
  - `GET /html/page/{type}` returns full panel fragments (`demographics`, `ai`, `georgia`).
  - `GET /html/section/{type}` returns sub-fragments (currently only `ai` via `ai_platform.html`).
- Templates live in `backend/templates/` and are rendered with Jinja2.
- Mock data is defined as Pydantic models + in-memory instances in `backend/main.py` and passed directly to templates.

## Essential commands
- No build/test/lint scripts found in the repository.
- `pyproject.toml` declares the FastAPI entrypoint as `backend.main:app` under `[tool.fastapi]`.

## Conventions & patterns
- Templates expect specific context keys:
  - `demographics.html` expects `statList`.
  - `ai.html` expects `aiGuides` and `currentGuide`.
  - `ai_platform.html` expects `currentGuide` (used for HTMX partial refresh).
  - `georgia.html` expects `georgiaData`.
- Template directory is hard-coded in `backend/main.py` as `backend/templates`.

## Gotchas
- HTMX calls use same-origin relative paths under `/html/...`.
- `backend/templates/stats.html` references `stat.value`, but `StatCard` in `backend/main.py` only defines `graph` and `detail`. This template currently appears unused.

## Reference docs
- Product context and UX exploration are in `docs/` (e.g., `ARCHITECTURE.md`, `USER_FLOW.md`).
