import os
from flask import send_file
import io
from reportlab.pdfgen import canvas
from flask import Flask, render_template
import pandas as pd

import json


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

df = pd.read_csv(os.path.join(DATA_DIR, "district_profiles_classified_1.csv"))

df["District"] = df["District"].astype(str)

with open(os.path.join(DATA_DIR, "scenario_validation.json")) as f:
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


@app.route("/generate_pdf/<district_id>")
def generate_pdf(district_id):

    data = district_data.get(district_id)

    if not data:
        return "District not found"

    profile = data["profile"]
    scenarios = data["scenarios"]

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    y = 780

    p.drawString(100, y, f"District Report: {district_id}")
    y -= 30

    # -------------------
    # PROFILE
    # -------------------

    p.drawString(100, y, "District Profile")
    y -= 20

    p.drawString(120, y, f"Business Count: {profile['Business_Count']}")
    y -= 18

    p.drawString(120, y, f"Violations Count: {profile['Violations_Count']}")
    y -= 18

    p.drawString(120, y, f"Business Level: {profile['Business_Level (High/Low)']}")
    y -= 18

    p.drawString(120, y, f"Stress Level: {profile['Stress_Level (High/Low)']}")
    y -= 18

    p.drawString(120, y, f"District Type: {profile['District_Type']}")
    y -= 30

    # -------------------
    # SCENARIOS
    # -------------------

    p.drawString(100, y, "Scenarios")
    y -= 20

    for s in scenarios:

        p.drawString(120, y, f"{s['title']} (Fit Score: {s['fit_score']})")
        y -= 18

        for a in s["actions"]:
            p.drawString(140, y, f"- {a}")
            y -= 16

            if y < 100:
                p.showPage()
                y = 780

        y -= 10

    p.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"district_{district_id}_report.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


