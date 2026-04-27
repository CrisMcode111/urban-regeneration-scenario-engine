from langchain.tools import tool
from data_loader import load_data

# Load once (important!)
profile_dict, scenario_dict = load_data()


@tool
def get_district_profile(district_id: str) -> dict:
    """Get district profile data from CSV"""
    return profile_dict.get(district_id, {})


@tool
def get_district_scenarios(district_id: str) -> list:
    """Get scenarios for a district"""
    return scenario_dict.get(district_id, [])


@tool
def get_full_district_data(district_id: str) -> dict:
    """Get full district data (profile + scenarios)"""
    return {
        "profile": profile_dict.get(district_id, {}),
        "scenarios": scenario_dict.get(district_id, [])
    }