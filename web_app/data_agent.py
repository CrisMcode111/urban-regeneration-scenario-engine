from typing import TypedDict, List, Dict

from openai import OpenAI



class UrbanState(TypedDict):
    """Defining a class for state to be defined accurately, an UrbanState object will have the key parameters of
    a district like ID, urban_stress and business_activity"""
    district_id: str
    business_activity: float
    urban_stress: float
    typology: str
    analysis: str
    scenarios: List[Dict]
    validation: str
    history: List[str]


# Defining LLM to invoke the agent
llm = OpenAI(model="gpt-4o-mini")


def data_analyst_node(state: UrbanState):

    prompt = f"""
    Analyze this district:
    Business Activity: {state['business_activity']}
    Urban Stress: {state['urban_stress']}

    Explain what this means in urban planning terms.
    """

    response = llm.predict(prompt)

    return {**state, "analysis": response}

