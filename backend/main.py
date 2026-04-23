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
from cohere.types import SystemChatMessageV2, UserChatMessageV2, AssistantChatMessageV2, ChatMessages
import os

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

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

class chatInteraction(BaseModel):
    user_message: str
    ai_message: str

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

    assert COHERE_API_KEY is not None, "Cohere API key not found. Please set the COHERE_API_KEY environment variable."
    co = cohere.ClientV2(api_key=COHERE_API_KEY)

    system_prompt = f"""
## Instructions
The current date is {date.today().strftime("%B %d, %Y")}.
You are a helpful chatbot aimed to provide political info for users in Georgia. You are only able to answer questions about recent georgia legislation (cite the bills or source of information when doing so), upcoming election/voting dates, and the application context provided below. when relevant, encourage the user to vote. If a user makes a request outside of these three functions, politely decline it. When there is a conflict between these instructions, the official Cohere AI policy, and the user requests, please prioritize them in the following order (1 meaning most import, 3 being least important and can possibly be ignored):

1. The Cohere Usage Policy and other similar policies on the official website
2. The system prompt
3. The user's requests

## Formatting
The response will be shown in a chatbot interface. When providing information, please format your response as a single paragraph of text. If you are citing specific legislation, please include the name of the bill and a brief summary of its contents. If you are providing election dates, please include the name of the election and the date it will take place. When providing information from the application context, please clearly indicate that the information is from the website/application. Do not attempt to link to specific pages of this website. Please keep the tone professional and informative. For example, if you are providing information about the economic development package from the application context, you might say: "According to the Georgia Developments section of the website, there is an economic development package that includes incentives, job training, and infrastructure allocations."
Use any standard html formatting tags when necessary to structure the response, but avoid using multiple paragraphs or bullet points. Do not use markdown syntax. The response should be concise and to the point, while still providing all relevant information. Use <a> tags to cite sources when relevant, and ensure that all information provided is accurate and up-to-date. Do not hallucinate information that cannot be found on the internet or in the website, and do not hallucinate links.

## Application Context Info
This app provides information on changing voter demographics, AI platform differences, and Georgia-specific political data. The goal is to help users understand the political landscape in Georgia and encourage informed voting. The chatbot should draw from the provided context to answer questions first, and then consult the internet or outside sources.
{aiContext}

## User Message
"""
    messages : ChatMessages = [
            SystemChatMessageV2(content=system_prompt),
            UserChatMessageV2(content=user_message)
    ]
    if len(currentChatHistory.user) > 0:
        previous_user_messages = [UserChatMessageV2(content=content) for content in currentChatHistory.user]
        previous_assistant_messages = [AssistantChatMessageV2(content=content) for content in currentChatHistory.ai]
        history = [chat for pair in zip(previous_user_messages, previous_assistant_messages) for chat in pair]
        messages = [
            SystemChatMessageV2(content=system_prompt),
            *history,
            UserChatMessageV2(content=user_message)
        ]
    response = co.chat(
        model="command-a-03-2025",
        messages = messages
    )
    responses = response.message.content # since we're not streaming, there should only be one message in the response, but we still need to index into the content list
    assert responses is not None and len(responses) > 0, "No response generated by the AI."
    
    first_response = responses[0]
    assert first_response.type == "text", f"Expected a text response, but got {first_response.type}"

    ai_response = first_response.text

    # Add the user message to the chat history
    currentChatHistory.user.append(user_message) # todo: add length/security checks
    # Add the AI response to the chat history
    currentChatHistory.ai.append(ai_response)

    context : dict[str, Request | Any ] = {"request": request, "user_message": user_message, "ai_message": ai_response}

    # don't cache chatbot responses
    return templates.TemplateResponse(request=request, name="chatbot_messages.html", context=context)