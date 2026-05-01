from datetime import date
from pathlib import Path
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request, HTTPException, Response, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

import cohere
from cohere.types import SystemChatMessageV2, UserChatMessageV2, AssistantChatMessageV2, ChatMessages, ToolV2, ToolV2Function, ToolChatMessageV2
import os

from backend.documents import ALL_DOCUMENTS
from backend.tools import describe


COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MGA_TITLE_IX_URL = "https://www.mga.edu/title-ix/"

app = FastAPI()

TEMPLATE_DIR = "backend/templates"
STATIC_DIR = "backend/static"
templates = Jinja2Templates(directory=TEMPLATE_DIR)
ROOT_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT_DIR / "htmx_index.html"
CACHE_HEADER = {"Cache-Control": "public, max-age=3600"}  # Cache for 1 hour
HEADERS = CACHE_HEADER

class StatCard(BaseModel):
    title: str
    graph: str | None = None # html snippet for graph, optional
    detail: str

class StatList(BaseModel):
    current_dataset: str
    stats: list[StatCard]
    insights: list[str] = []

class AiGuide(BaseModel):
    label: str
    summary: str
    bias: str
    distribution: str

class AiGuideList(BaseModel):
    guides: dict[str, AiGuide]

class GeorgiaLaw(BaseModel):
    title: str
    detail: str

class GeorgiaPoll(BaseModel):
    subject: str
    value: int
    detail: str

class GeorgiaOfficial(BaseModel):
    name: str
    role: str
    contact: str

class GeorgiaData(BaseModel):
    laws: list[GeorgiaLaw]
    polls: list[GeorgiaPoll]
    officials: list[GeorgiaOfficial]

class chatHistory(BaseModel):
    user: list[str]
    ai: list[str]

class CitationLink(BaseModel):
    title: str
    url: str

class chatInteraction(BaseModel):
    user_message: str
    ai_message: str
    citations: list[CitationLink] = []

currentChatHistory = chatHistory(user=[], ai=[])
stat1 = StatCard(title="Households under $75k", detail="Budget-aware messaging needed.", graph="<div class='bar'><span style='--value: 47%'></span></div>")

stat2 = StatCard(title="Digital-first news", detail="Social and mobile news consumption.", graph="<div class='bar'><span style='--value: 58%'></span></div>")
insights1 = [
    "Metro Atlanta remains the highest growth corridor for persuadable voters.",
    "Economic security is the top driver across suburban swing precincts.",
    "Faith and local community networks still outperform paid digital in rural counties.",
]
myStats : StatList = StatList(current_dataset="voting-age-adults", stats=[stat1, stat2], insights=insights1)

aiGuides : dict[str, AiGuide] = {
    "grok": AiGuide(
        label="X / Grok",
        summary="Grok is positioned as a less filtered summarizer that draws from X posts and web sources. Its main quality is directness.",
        bias="Public prompt files emphasize avoiding labeling political viewpoints as biased and assuming subjective sources are biased. It is less restricted than the other chatbots and somewhat distrustful of mainstream media outlets. According to X, it will not \"moralize or lecture the user if they ask something edgy.\"",
        distribution="X ranking favors engagement velocity, repost chains, and freshness. Content framing should anticipate summarizer snippets and trending-topic context.",
    ),
    "meta": AiGuide(
        label="Meta AI / Llama-based assistants",
        summary="Meta assistants typically summarize with safety-weighted, moderation-forward answers and cite community guidelines more often.",
        bias="Responses often prioritize safety policy and de-escalation. Messaging may be reframed if it triggers sensitive topic classifiers.",
        distribution="Meta feed delivery is heavily influenced by relationship graphs, watch time, and content type mixing. Emphasize authentic community engagement signals.",
    ),
    "google": AiGuide(
        label="Google / Gemini-style summaries",
        summary="Search-integrated assistants synthesize across authoritative sources and structure responses around consensus and citations.",
        bias="Tends to weight institutional sources and down-rank unsupported claims. Messaging should anticipate fact-check style framing.",
        distribution="Visibility is tied to search intent signals, quality ratings, and content freshness. Use clear headings and structured metadata.",
    ),
}

georgiaData = GeorgiaData(
    laws=[
        GeorgiaLaw(title="Bill allows compensation for home owners who believe anti-homless policies are not being enforced", detail="Critics believe enforcement resources should be better spent on housing and support; Proponents believe property owners should be compensated for losses/damages due to nearby encampments."),
        GeorgiaLaw(title="Increased regulations for HOAs", detail="SB 406 requires HOAs to register with the Secretary of State to collect fees; The threshold necessary for an HOA file a lien against a homeowner was doubled to $4,000"),
        GeorgiaLaw(title="Wildfires lead to state of emergency", detail="Gov. Kemp has declared a state of emergency for over half of Georgia's counties, along with a temporary ban on outdoor burning"),
    ],
    polls=[
        GeorgiaPoll(subject="Top issue: Cost of living", value=72, detail="Sample pulse across likely voters."),
        GeorgiaPoll(subject="Support for transit expansion", value=55, detail="Higher in metro counties."),
        GeorgiaPoll(subject="Trust in local leaders", value=48, detail="Mixed sentiment; needs validation."),
    ],
    officials=[
        GeorgiaOfficial(name="Governors Office", role="Executive leadership", contact="Sample contact: 404-555-0110 • governor@example.gov"),
        GeorgiaOfficial(name="Secretary of State", role="Elections administration", contact="Sample contact: 404-555-0182 • elections@example.gov"),
        GeorgiaOfficial(name="State Senate Majority", role="Legislative agenda", contact="Sample contact: 404-555-0195 • senate@example.gov"),
    ],
)


# todo: find better way to share chatbot context between pages:
# combine all of the variables in this file into a json object
aiContext : dict[str, AiGuideList | StatList | GeorgiaData] = {
    "myStats": myStats,
    "aiGuides": AiGuideList(guides=aiGuides),
    "georgiaData": georgiaData
}

# serve static css and js files from the `static` directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=FileResponse)
async def return_index() -> FileResponse:
    return FileResponse(INDEX_PATH, media_type="text/html")

@app.get("/html/page/{type}", response_class=HTMLResponse)
async def return_page(response: Response, request: Request, type: str) -> HTMLResponse:
    match type:
        case "demographics":
            template_name = "demographics.html"
            context : dict[str, Request | Any ] = {"request": request, "statList": myStats}
        case "ai":
            template_name = "ai.html"
            context  = {"request": request, "aiGuides": aiGuides, "currentGuide": next(iter(aiGuides.values()))}
        case "georgia":
            template_name = "georgia.html"
            context = {"request": request, "georgiaData": georgiaData}
        case _:
            raise HTTPException(status_code=404, detail="Template not found")
        
    return templates.TemplateResponse(request=request, name=template_name, context=context, headers=HEADERS)

@app.get("/html/section/{type}", response_class=HTMLResponse)
async def return_section(response: Response, request: Request, type: str, ai: str | None = None) -> HTMLResponse:
    match (type, ai in aiGuides):
        case "ai", True:
            assert ai is not None  # for pydantic
            template_name = "ai_platform.html"
            context : dict[str, Request | Any ] = {"request": request, "currentGuide": aiGuides.get(ai)}
        case "chatbot", _:
            template_name = "chatbot.html"
            context = {"request": request, "aiContext": aiContext, "chatHistory": currentChatHistory}
        case _:
            raise HTTPException(status_code=404, detail="Template subsection not found")
    
    return templates.TemplateResponse(request=request, name=template_name, context=context, headers=HEADERS)

@app.post("/chatbot/message", response_class=HTMLResponse)
async def receive_message(request: Request, user_message: str = Form()) -> HTMLResponse:
    global currentChatHistory
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

You must ground every response in the provided documents. If the answer to a question cannot be found in the provided documents, clearly state that the information is not available in the provided documents and direct the user to contact MGA's Title IX Coordinator or visit {MGA_TITLE_IX_URL} for the most current information.

If a user asks about something outside of Title IX at MGA, politely decline and explain that you can only assist with MGA Title IX-related questions.

When there is a conflict between these instructions and the official Cohere AI policy, prioritize the Cohere Usage Policy first, then these instructions.

## Formatting
Format your response as clear, readable HTML for display in a chat interface. Use plain sentences. You may use <strong> for emphasis on key terms. Do not use markdown. Do not use multiple paragraphs unless necessary. Keep the response concise and professional. Do not add <a> tags in your response text — citations will be shown separately below your response.

When information comes from a document, you MUST cite it. Inline citation markers like [1] or [Doc: MGA Title IX Policy] are not required in the text itself — the citation system will handle linking sources automatically. Focus on accuracy and clarity.
"""

    messages: ChatMessages = [
        SystemChatMessageV2(content=system_prompt),
        UserChatMessageV2(content=user_message),
    ]

    if len(currentChatHistory.user) > 0:
        previous_user_messages = [UserChatMessageV2(content=content) for content in currentChatHistory.user]
        previous_assistant_messages = [AssistantChatMessageV2(content=content) for content in currentChatHistory.ai]
        history = [chat for pair in zip(previous_user_messages, previous_assistant_messages) for chat in pair]
        messages = [
            SystemChatMessageV2(content=system_prompt),
            *history,
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
        tools=[describe_tool]
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
    currentChatHistory.user.append(user_message)  # todo: add length/security checks
    currentChatHistory.ai.append(ai_response)

    context: dict[str, Request | Any] = {
        "request": request,
        "user_message": user_message,
        "ai_message": ai_response,
        "citations": citations,
        "tool_calls_made": tool_calls_made
    }

    # don't cache chatbot responses
    return templates.TemplateResponse(request=request, name="chatbot_messages.html", context=context)