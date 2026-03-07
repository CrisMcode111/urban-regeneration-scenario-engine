import os

from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

df = pd.read_csv("../data/district_profiles_classified_1.csv")
df["District"] = df["District"].astype(str)

with open("../data/scenario_validation.json") as f:
    scenarios = json.load(f)

# convert scenarios list → dictionary
scenario_dict = {d["district"]: d["scenario"] for d in scenarios}

district_data = {}

for _, row in df.iterrows():

    district_id = str(row["District"])

    profile = row.to_dict()
    scen = scenario_dict.get(district_id, [])

    best = max(scen, key=lambda x: x["fit_score"], default=None)

    district_data[district_id] = {
        "profile": profile,
        "scenarios": scen,
        "best": best
    }

@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        district_data=json.dumps(district_data)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


