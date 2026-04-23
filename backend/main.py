from typing import Any

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

app = FastAPI()

TEMPLATE_DIR = "backend/templates"
templates = Jinja2Templates(directory=TEMPLATE_DIR)

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

stat1 = StatCard(title="Race diversity index", detail="Higher mix across metro & rural counties.", graph="<div class='bar'><span style='--value: 65%'></span></div>")
stat2 = StatCard(title="Women voters", detail="Estimated share of voting-age adults.", graph="<div class='bar'><span style='--value: 53%'></span></div>")
stat3 = StatCard(title="Households under $75k", detail="Budget-aware messaging needed.", graph="<div class='bar'><span style='--value: 47%'></span></div>")
stat4 = StatCard(title="Digital-first news", detail="Social and mobile news consumption.", graph="<div class='bar'><span style='--value: 58%'></span></div>")
insights1 = [
    "Metro Atlanta remains the highest growth corridor for persuadable voters.",
    "Economic security is the top driver across suburban swing precincts.",
    "Faith and local community networks still outperform paid digital in rural counties.",
]
myStats : StatList = StatList(current_dataset="voting-age-adults", stats=[stat1, stat2, stat3, stat4], insights=insights1)

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
        GeorgiaLaw(title="Election administration updates", detail="Mock item: track new rule changes, early voting windows, and ballot processing shifts."),
        GeorgiaLaw(title="Economic development package", detail="Mock item: monitor incentives, job training, and infrastructure allocations."),
        GeorgiaLaw(title="Education funding proposals", detail="Mock item: watch committee hearings and local district impacts."),
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

@app.get("/html/page/{type}", response_class=HTMLResponse)
async def return_page(request: Request, type: str) -> HTMLResponse:
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

    return templates.TemplateResponse(request=request, name=template_name, context=context)

@app.get("/html/section/{type}", response_class=HTMLResponse)
async def return_section(request: Request, type: str, ai: str) -> HTMLResponse:
    match type:
        case "ai":
            template_name = "ai_platform.html"
            context : dict[str, Request | Any ] = {"request": request, "currentGuide": aiGuides.get(ai)}
        case _:
            raise HTTPException(status_code=404, detail="Template subsection not found")

    return templates.TemplateResponse(request=request, name=template_name, context=context)
