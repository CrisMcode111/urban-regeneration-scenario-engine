import folium
import geopandas as gpd

# Load district boundaries
gdf = gpd.read_file("montgomery_districts.geojson")
print(gdf[["District","Name"]])

data = gpd.read_csv("data/district_data.csv")

gdf = gdf.merge(data, on="DISTRICT")

# Center map roughly on Montgomery
m = folium.Map(location=[32.37, -86.30], zoom_start=11)

# Add all districts at once
folium.GeoJson(
    gdf,
    name="Districts",
    tooltip=folium.GeoJsonTooltip(
        fields=["District","Name"],
        aliases=["District:", "Council Member:"]
    )
).add_to(m)

m.save("montgomery_all_districts_map.html")