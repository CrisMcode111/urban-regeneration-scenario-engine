import os
import pandas as pd
import json

# go UP from web_app → project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

def load_data():
    # --- Load CSV ---
    df = pd.read_csv(os.path.join(DATA_DIR, "district_profiles_classified_1.csv"))
    df["District"] = df["District"].astype(str)

    profile_dict = df.set_index("District").to_dict(orient="index")

    # --- Load JSON ---
    with open(os.path.join(DATA_DIR, "scenario_validation.json")) as f:
        scenarios = json.load(f)

    scenario_dict = {d["district"]: d["scenario"] for d in scenarios}

    return profile_dict, scenario_dict