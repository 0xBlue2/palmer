# Palmer Project - Agent Guidelines

## Overview
This is a FastAPI-based web application with an HTMX and Alpine.js frontend, styled with PicoCSS. It serves as a mock campaign intelligence dashboard featuring a demographic analyzer, AI platform guides, and a Georgia political development tracker. It also includes an AI chatbot powered by Cohere, focused on Title IX information at Middle Georgia State University (MGA).

## Tech Stack
- **Backend**: FastAPI, Python 3
- **Frontend**: HTML, HTMX (for dynamic partial loading), Alpine.js (for simple state/UI interactions), PicoCSS (for styling)
- **Templating**: Jinja2
- **AI**: Cohere API (`cohere` python package)
- **Deployment**: Docker, configured for fly.io

## Code Organization & Architecture

### Backend (`/backend`)
- `main.py`: The core FastAPI application. Handles routing, template rendering (both HTML and Markdown), static file serving, and the chatbot endpoint (`/chatbot/message`).
- `documents.py`: Contains the document stubs (MGA Title IX policies, Clery Report, USG policies, and parsed website resources) used for Retrieval-Augmented Generation (RAG) by the Cohere chatbot.
- `tools.py`: (Assumed) Contains tools available to the AI, such as `describe` for the mock Macon statistics.
- `templates/`: Jinja2 templates.
  - `base.html`: The base layout.
  - `chatbot_messages.html`: Partial template for rendering a chat message and citations.
  - `pages/`: Directory containing dynamic pages. The app automatically serves `.html` or `.md` files found here at the `/{template}` route. Markdown files are parsed with `mistune`.
- `static/`: Static assets (JS, CSS).

### Frontend (`/index.html` & `templates/`)
- Relies on HTMX for fetching sections of the page without full reloads (e.g., loading different panels)

## Key Patterns & Gotchas

### Template Rendering
- The backend has custom logic (`render_template` in `main.py`) to automatically detect and serve either `.html` or `.md` files from the `backend/templates/pages` directory. 
- If a `.md` file is requested, it is read, parsed to HTML using `mistune`, wrapped in a base template block, and rendered as a Jinja string.
- This means you can create a new page just by dropping an HTML or Markdown file into the `pages/` directory.

### Chatbot Architecture
- The chatbot uses the **Cohere V2 API** (`cohere.ClientV2`).
- **Global State Gotcha:** The chat history (`messages: ChatMessages = []` in `main.py`) is stored in a **global variable**. This means the chat history is shared across *all* requests and users. This is currently by design for the mock/demo, but it's a critical architectural detail.
- **RAG & Citations:** The chatbot is grounded in specific documents defined in `backend/documents.py`. It uses Cohere's document capabilities and extracts citations. The `chatbot_messages.html` template handles displaying these citations below the AI response.
- **Tool Calling:** The chatbot supports tool calls (e.g., `describe_macon_statistics`). The logic for handling these is explicitly written out in the `/chatbot/message` route rather than abstracted away.

## Essential Commands

### Local Development
```bash
# Activate virtual environment (Windows syntax shown in Makefile)
.\venv\Scripts\activate

# Run the FastAPI server with hot-reload
uvicorn backend.main:app --reload
```
*Alternatively, you can run `make run` if you have Make installed.*

### Docker
```bash
# Build the Docker image
docker build -t palmer .

# Run the Docker container locally
docker run -p 8000:8000 --env-file .env palmer
```
*Alternatively, use `make build` and `make run-docker`.*

## Environment Variables
- `COHERE_API_KEY`: Required for the chatbot to function.

## Future Agents Note
When editing `main.py` or the template logic, pay close attention to the paths relative to the Jinja environment vs. absolute paths on the filesystem, as the custom template loader handles both to support the markdown-to-html feature.