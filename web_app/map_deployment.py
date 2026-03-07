import pandas as pd
import folium

# District data
data = {
    "district": [
        "DISTRICT 1", "DISTRICT 2", "DISTRICT 3",
        "DISTRICT 4", "DISTRICT 5", "DISTRICT 6",
        "DISTRICT 7", "DISTRICT 8", "DISTRICT 9"
    ],

    "latitude": [
        32.3585, 32.4312, 32.4230,
        32.2547, 32.2141, 32.1341,
        32.2807, 32.2064, 32.2781
    ],

    "longitude": [
        -86.2957, -86.3075, -86.4520,
        -86.5862, -86.3727, -86.3048,
        -86.4941, -86.1860, -86.1276
    ]
}

df = pd.DataFrame(data)

# Create map centered on Montgomery
m = folium.Map(location=[32.36, -86.30], zoom_start=10)

# Add markers
for i in range(len(df)):
    folium.Marker(
        location=[df.latitude[i], df.longitude[i]],
        popup=df.district[i],
        tooltip=df.district[i]
    ).add_to(m)

# Save map
m.save("static/maps/montgomery_districts_map.html")

print("Map created: montgomery_districts_map.html")
