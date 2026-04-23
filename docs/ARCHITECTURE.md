# Architecture

## Idea 1: HTMX / HATEOAS
- use http methods and receive html snippets from the backend
frontend: htmx
backend: python - fastapi  with jinja2 templates  (could be any language but we want easy data analysis libraries)

pros:
- easy(?) templating
- should be able to run df.describe().to_html() and send it to the client
cons:
- need display logic on front and backend
- will eventually have to rewrite/separate data from display logic when I move to a json-based API
- might be hard getting editor support with j2 templates?
- to follow htmx pattern, graphs are built on server and sent to client (but we would already have to do this for huge datasets, unless we downsample)

## Idea 2 - Generic (RESTful?) API with json
- send and receive json
- for large datasets, downsample on backend before sending to client
pros: more "normal," API logic/insights separated from frontend/graphing code
