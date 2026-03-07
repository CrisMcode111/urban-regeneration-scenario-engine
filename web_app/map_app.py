import folium
import geopandas as gpd
import json
import pandas as pd

# ----------------------------
# Load spatial data
# ----------------------------
districts = gpd.read_file("../data/montgomery_districts.geojson")

# ----------------------------
# Load CSV profile data
# ----------------------------
df = pd.read_csv("../data/district_profiles_classified_1.csv")

# Make district column string
df["District"] = df["District"].astype(str)

# Convert to dictionary for fast lookup
profile_dict = df.set_index("District").to_dict(orient="index")

# ----------------------------
# Load scenario data
# ----------------------------
with open("../data/scenario_validation.json", "r") as f:
    scenarios = json.load(f)

scenario_dict = {d["district"]: d for d in scenarios}

# ----------------------------
# Create map
# ----------------------------
m = folium.Map(location=[32.37, -86.30], zoom_start=11)


# ----------------------------
# Color districts based on Stress Level
# ----------------------------
def get_color(district_id):
    if district_id in profile_dict:
        stress = profile_dict[district_id]["Stress_Level (High/Low)"]
        if stress == "High":
            return "red"
        else:
            return "green"
    return "gray"


# ----------------------------
# Loop through districts
# ----------------------------
for _, row in districts.iterrows():

    district_id = str(row["District"]).split()[-1]

    # ----------------------------
    # PROFILE SECTION (CSV)
    # ----------------------------
    profile_text = ""

    if district_id in profile_dict:
        profile = profile_dict[district_id]

        profile_text = f"""
        <h5>📊 District Profile</h5>
        <b>Business Count:</b> {profile["Business_Count"]}<br>
        <b>Violations:</b> {profile["Violations_Count"]}<br>
        <b>Business Level:</b> {profile["Business_Level (High/Low)"]}<br>
        <b>Stress Level:</b> {profile["Stress_Level (High/Low)"]}<br>
        <b>District Type:</b> {profile["District_Type"]}<br>
        <hr>
        """

    # ----------------------------
    # SCENARIO SECTION (JSON)
    # ----------------------------
    scenario_text = ""

    if district_id in scenario_dict:
        district_data = scenario_dict[district_id]

        scenario_text += "<h5>🚀 Scenarios</h5>"

        for s in district_data["scenario"]:
            actions = "<br>".join(s["actions"])

            scenario_text += f"""
            <b>{s['scenario_type']}</b><br>
            {s['title']} (Score: {s['fit_score']})<br>
            {actions}
            <br><br>
            """

    # ----------------------------
    # Combine popup
    # ----------------------------
    popup_html = f"""
    <h4>District {district_id}</h4>
    <hr>
    {profile_text}
    {scenario_text}
    """

    # ----------------------------
    # Add to map
    # ----------------------------
    folium.GeoJson(
        row["geometry"],
        tooltip=f"District {district_id}",
        popup=folium.Popup(popup_html, max_width=450),
        style_function=lambda x, district_id=district_id: {
            "fillColor": get_color(district_id),
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.5,
        },
    ).add_to(m)

# ----------------------------
# Save map
# ----------------------------
m.save("static/maps/montgomery_all_districts_analytics_map.html")

print("Map saved successfully")