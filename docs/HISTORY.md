# History

## Day 1
:star: had GPT-5.2-Codex vibe code the website, using alpinejs and picocss + mock data

Three main features (all insights/data mocked):
- demographic analyzer
  - select or upload a dataset and receive insights
- social media/AI guides
  - see how different social media chatbots and LLMS (Grok, Meta AI) summarize/rank text
- Georgia political development tracker
  - recent political developments in Georgia, and estimations of voter sentiment on them, when possible

## Day 2

:star: Added ARCHITECTURE.md, and decided to use htmx + fastapi
- had codex rewrite the frontend to fetch html (via htmx)
- also rewrite alpinejs templating to jinja2 templates, and create AGENTS.md
- researched deployment/library options:
  - current plan: deploy on fly.io, use langchain-python

## Day 3
:star: Deployed on fly.io, made some changes to how css/js is served for production, index file now served by fastapi
- fly.io platform automatically created dockerfile
- had docker ai (Gordon) rewrite Dockerfile
  - app no longer runs under superuser, healthcheck added, separate images for runtime vs production
- added caching via Cache-Control header
- rewrote index file to only fetch panel when panel button is clicked
  - still using alpinejs to manage aria-current and which panel is actively displayed
  - added hx-trigger="load, click" to first panel (demographics) so it's loaded automatically as well as when button is clicked