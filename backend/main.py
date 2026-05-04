from datetime import date
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request, HTTPException, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import jinja2
import mistune

import cohere
from cohere.types import SystemChatMessageV2, UserChatMessageV2, AssistantChatMessageV2, ChatMessages, ToolV2, ToolV2Function, ToolChatMessageV2
import os

from backend.documents import ALL_DOCUMENTS
from backend.tools import describe

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MGA_TITLE_IX_URL = "https://www.mga.edu/title-ix/"

app = FastAPI()

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT_DIR / "backend/templates"
RELATIVE_PATH_PAGES_DIR = "pages" # path relative to jinja2 env
FULL_PATH_PAGES_DIR = TEMPLATE_DIR / RELATIVE_PATH_PAGES_DIR
STATIC_DIR = ROOT_DIR / "backend/static"
INDEX_PATH = ROOT_DIR / "index.html"
CACHE_HEADER = {"Cache-Control": "public, max-age=0"}  # Cache for 0
HEADERS = CACHE_HEADER

jenv = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    autoescape=jinja2.select_autoescape(["html"])
)

jenv.globals = globals() # let jinja2 templates access libraries

templates = Jinja2Templates(env=jenv)



messages: ChatMessages = []


# serve static css and js files from the `static` directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def return_index(request: Request) -> HTMLResponse:
    return render_template("chatbot", request)
    
# helper function to check if a template exists in pages dir
def template_exists(template_name: str) -> bool:
    html_path = os.path.join(FULL_PATH_PAGES_DIR, f"{template_name}.html")
    md_path = os.path.join(FULL_PATH_PAGES_DIR, f"{template_name}.md")
    return os.path.isfile(html_path) or os.path.isfile(md_path)

# helper function to return template path given basename
def get_template_path(template_name: str) -> str:
    html_path = os.path.join(FULL_PATH_PAGES_DIR, f"{template_name}.html") # "pages/chatbot.html", relative to templates directory
    md_path = os.path.join(FULL_PATH_PAGES_DIR, f"{template_name}.md")
    if os.path.isfile(html_path): # return relative path
        return RELATIVE_PATH_PAGES_DIR + "/" + f"{template_name}.html"
    elif os.path.isfile(TEMPLATE_DIR / md_path): # return full path since md files have to be read manually
        return md_path
    else:
        return "" # for pydantic

# helper function to render template  with context given basename and request
def render_template(template_name: str, request: Request) -> HTMLResponse:
    if not template_exists(template_name):
        raise HTTPException(status_code=404, detail="Template not found")  
    context : dict[str, Request | Any ] = {
        "request": request,
        "files": os.listdir(FULL_PATH_PAGES_DIR),
        "currentPage": template_name
    }
    name = get_template_path(template_name)
    try: # try to render .html
        return templates.TemplateResponse(request=request, name=name, context=context, headers=HEADERS)
    except jinja2.TemplateNotFound: # assuming markdown
        # read from file and convert markdown to html
        with open(FULL_PATH_PAGES_DIR / name, "r", encoding="utf-8") as f:
            content = f.read()
            md = mistune.html(content)
            assert type(md) == str, "Expected mistune to return a string of HTML"
            md = "{% extends 'base.html' %}\n{% block content %}" + md + "\n{% endblock %}"
            rendered_html = jenv.from_string(md).render(context)
            return HTMLResponse(content=rendered_html, headers=HEADERS)
    
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
    assert COHERE_API_KEY is not None, "Cohere API key not found. Please set the COHERE_API_KEY environment variable."
    co = cohere.ClientV2(api_key=COHERE_API_KEY)


    system_prompt = f"""
## Instructions
The current date is {date.today().strftime("%B %d, %Y")}.
You are a helpful assistant focused exclusively on Title IX information at Middle Georgia State University (MGA). You can only answer questions about:
1. MGA's Title IX policies and procedures
2. MGA's Annual Security and Fire Safety Report (Clery Report)
3. The University System of Georgia sexual misconduct policy as it applies to MGA
4. Resources available to MGA community members regarding Title IX matters

## Formatting / Style
Format your response as clear, readable HTML for display in a chat interface. Use plain sentences. Do not use markdown. Do not use multiple paragraphs unless necessary. Keep the response concise and professional. Do not add <a> tags in your response text — citations will be shown separately below your response.
When using documents, summarize the relevant information in your own words. Do not copy and paste large sections of text. Translate any technical or legal language into clear, plain language that is easy to understand. When reading markdown documents, be sure to interpret the markdown formatting correctly (e.g. lists, tables) and include that formatting in your response when relevant. Example: if the relevant information is presented as a list in the document, present it as a list(using <ul> and <li> tags) in your response.

When information comes from a document, you MUST cite it. Do not include inline citation markers like [1] or [Doc: MGA Title IX Policy]  — the citation system will handle linking sources automatically. Focus on accuracy and clarity.

## Important Notes
You must ground every response in the provided documents. If the answer to a question cannot be found in the provided documents, clearly state that the information is not available in the provided documents and direct the user to contact MGA's Title IX Coordinator or visit {MGA_TITLE_IX_URL} for the most current information.

If a user asks about something outside of Title IX at MGA, politely decline and explain that you can only assist with MGA Title IX-related questions.

When there is a conflict between these instructions and the official Cohere AI policy, prioritize the Cohere Usage Policy first, then these instructions.
"""

    messages = [
        SystemChatMessageV2(content=system_prompt),
        UserChatMessageV2(content=user_message),
    ]

    describe_tool = ToolV2(
        type="function",
        function=ToolV2Function(
            name="describe_macon_statistics",
            description="Returns descriptive statistics of crime data for Macon.",
            parameters={}
        )
    )

    response = co.chat(
        model="command-a-03-2025",
        messages=messages,
        documents=ALL_DOCUMENTS,
        # tools=[describe_tool]
        # citation_options=CitationOptions(mode="accurate"),
    )

    tool_calls_made: list[str] = []

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            assert tool_call.function != None
            if tool_call.function.name == "describe_macon_statistics":
                tool_calls_made.append("describe_macon_statistics")
                tool_results = describe().to_dict()
                messages.append(AssistantChatMessageV2(tool_calls=[tool_call]))
                messages.append(ToolChatMessageV2(tool_call_id=tool_call.id, content=str(tool_results)))
                
        response = co.chat(
            model="command-a-03-2025",
            messages=messages,
            documents=ALL_DOCUMENTS,
            tools=[describe_tool]
        )

    # Extract text response
    responses = response.message.content
    assert responses is not None and len(responses) > 0, "No response generated by the AI."
    first_response = responses[0]
    assert first_response.type == "text", f"Expected a text response, but got {first_response.type}"
    ai_response = first_response.text

    # Extract unique cited sources from citations
    seen_doc_ids: set[str] = set()
    citations: list[dict[str, str]] = []
    raw_citations = response.message.citations or []
    for citation in raw_citations:
        for source in (citation.sources or []):
            if source.type == "document":
                doc_id = source.id or ""
                if doc_id not in seen_doc_ids:
                    seen_doc_ids.add(doc_id)
                    doc_data = source.document or {}
                    title = doc_data.get("title", "Source")
                    url = doc_data.get("url", "")
                    if url:
                        citations.append({"title": title, "url": url})

    # Add the user message and AI response to the chat history
    messages.append(UserChatMessageV2(content=user_message))  # todo: add length/security checks
    messages.append(AssistantChatMessageV2(content=ai_response))

    context: dict[str, Request | Any] = {
        "request": request,
        "user_message": user_message,
        "ai_message": ai_response,
        "citations": citations,
        "tool_calls_made": tool_calls_made
    }

    # don't cache chatbot responses
    print(messages)
    return templates.TemplateResponse(request=request, name="chatbot_messages.html", context=context)