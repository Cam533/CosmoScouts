import folium
from folium.plugins import HeatMap


def generate_heatmap(locations):
    # locations is a list of tuples (lat, lon, visibility_score)
    map = folium.Map(location=[0, 0], zoom_start=2)
    HeatMap(locations).add_to(map)
    # Save to file (consider saving with a unique name or to a database)
    map.save('heatmap.html')
    # Return the path or a URL to access the heatmap
    return 'path/to/heatmap.html'