from flask import Flask
from flask import Flask, request, jsonify
import asyncio
import python_weather
import asyncio
import os
import folium


app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def weather():
    location = request.args.get('location')
    weather_info = asyncio.run(get_weather_conditions(location))
    return jsonify(weather_info)

@app.route('/api/heatmap', methods=['POST'])
def heatmap():
    locations = request.json['locations']
    heatmap_url = generate_heatmap(locations)
    return jsonify({'heatmap_url': heatmap_url})

if __name__ == '__main__':
    app.run(debug=True)