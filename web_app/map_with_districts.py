import folium
import geopandas as gpd
import json

# Load district boundaries
districts = gpd.read_file("montgomery_districts.geojson")


# load scenario file
with open("../data/scenario_validation.json", "r") as f:
    scenarios = json.load(f)

# Convert JSON to dictionary
scenario_dict = {d["district"]: d for d in scenarios}

# Center map roughly on Montgomery
m = folium.Map(location=[32.37, -86.30], zoom_start=11)

# function for styling the districts(optional)
def style_function(feature):
    return {
        "fillColor": "#3186cc",
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.4
    }

for _, row in districts.iterrows():

    district_id = str(row["District"]).split()[-1]   # extract 1,2,3...

    scenario_text = ""

    if district_id in scenario_dict:
        district_data = scenario_dict[district_id]

        for s in district_data["scenario"]:
            actions = "<br>".join(s["actions"])

            scenario_text += f"""
            <b>{s['scenario_type']}</b><br>
            {s['title']} (score: {s['fit_score']})<br>
            {actions}<br><br>
            """

    popup_html = f"""
    <h4>District {district_id}</h4>
    {scenario_text}
    """

    folium.GeoJson(
        row["geometry"],
        tooltip=f"District {district_id}",
        popup=folium.Popup(popup_html, max_width=400),
        style_function=lambda x:{
            "fillColor":"blue",
            "color":"black",
            "weight":1,
            "fillOpacity":0.4
        }
    ).add_to(m)


m.save("montgomery_all_districts_map.html")