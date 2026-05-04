from typing import Any

from fastapi import FastAPI, Request, HTTPException, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from cohere.types import UserChatMessageV2, AssistantChatMessageV2, ChatMessages

from backend.tools import *
from backend.CONSTANTS import *
from backend.template_setup import templates
from backend.helpers import template_exists, render_template, chat

app = FastAPI()


# user and AI message history
messages: ChatMessages = []


# serve static css and js files from the `static` directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def return_index(request: Request) -> HTMLResponse:
    return render_template("chatbot", request)

@app.get("/{template}", response_class=HTMLResponse)
async def return_page(response: Response, request: Request, template: str) -> HTMLResponse:
    if not template_exists(template):
        raise HTTPException(status_code=404, detail="Template not found")  
    return render_template(template, request)

@app.get("/html/section/{type}", response_class=HTMLResponse)
async def return_section(response: Response, request: Request, type: str, ai: str | None = None) -> HTMLResponse:
    match type:
        case "chatbot":
            template_name = "chatbot.html"
            context : dict[str, Request | Any ] = {"request": request}
        case _:
            raise HTTPException(status_code=404, detail="Template subsection not found")
    
    return templates.TemplateResponse(request=request, name=template_name, context=context, headers=HEADERS)

@app.post("/chatbot/message", response_class=HTMLResponse)
async def receive_message(request: Request, user_message: str = Form()) -> HTMLResponse:
    global messages
    context = chat(user_message, request)
    messages.append(UserChatMessageV2(content=user_message))
    messages.append(AssistantChatMessageV2(content=context.get("ai_message")))

    # don't cache chatbot responses
    return templates.TemplateResponse(request=request, name="chatbot_messages.html", context=context)