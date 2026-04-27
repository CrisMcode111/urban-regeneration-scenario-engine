from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

from tools import get_full_district_data

from dotenv import load_dotenv
import os

load_dotenv()   # <-- THIS MUST COME BEFORE ChatOpenAI

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")  # explicit (safer)
)


class UrbanState(TypedDict):
    district_id: str
    data: Dict
    analysis: str
    scenarios: List[Dict]
    validation: str
    history: List[str]


# -----------------------------
# Node 1: Fetch Data (Tool Usage)
# -----------------------------
def fetch_data_node(state: UrbanState):

    data = get_full_district_data.invoke(state["district_id"])

    state["data"] = data
    state["history"].append("Fetched district data")

    return state


# -----------------------------
# Node 2: Analysis
# -----------------------------
def analysis_node(state: UrbanState):

    profile = state["data"]["profile"]

    prompt = f"""
    You are an urban planning expert.

    District Data:
    {profile}

    Explain:
    - Current condition
    - Risks
    - Opportunities
    """

    response = llm.invoke(prompt).content

    state["analysis"] = response
    state["history"].append("Analysis done")

    return state


# -----------------------------
# Node 3: Scenario Generation
# -----------------------------
def scenario_node(state: UrbanState):

    prompt = f"""
    Based on this analysis:

    {state['analysis']}

    Generate 3 strategies:
    - Stabilization
    - Economic Activation
    - Public Space

    Return structured JSON.
    """

    response = llm.invoke(prompt).content

    state["scenarios"] = response
    state["history"].append("Scenarios generated")

    return state


# -----------------------------
# Node 4: Validation
# -----------------------------
def validation_node(state: UrbanState):

    prompt = f"""
    Validate these strategies:

    {state['scenarios']}

    Based on:
    {state['analysis']}

    Answer:
    VALID or INVALID + reason
    """

    response = llm.invoke(prompt).content

    state["validation"] = response
    state["history"].append("Validation done")

    return state


# -----------------------------
# Decision Edge
# -----------------------------
def should_retry(state: UrbanState):
    if "INVALID" in state["validation"]:
        return "retry"
    return "end"


# -----------------------------
# Build Graph
# -----------------------------
builder = StateGraph(UrbanState)

builder.add_node("fetch", fetch_data_node)
builder.add_node("analysis", analysis_node)
builder.add_node("scenario", scenario_node)
builder.add_node("validation", validation_node)

builder.set_entry_point("fetch")

builder.add_edge("fetch", "analysis")
builder.add_edge("analysis", "scenario")
builder.add_edge("scenario", "validation")

builder.add_conditional_edges(
    "validation",
    should_retry,
    {
        "retry": "scenario",
        "end": END
    }
)

graph = builder.compile()