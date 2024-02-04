from flask import Flask
from flask import Flask, request, jsonify
import asyncio
from weather_conditions import get_weather_conditions
import asyncio


app = Flask(__name__)

@app.route('/api/weather', methods=['POST'])
def weather():
    data = request.get_json()
    location = data.get('city')
    weather_info = asyncio.run(get_weather_conditions(location))
    return jsonify(weather_info)

@app.route('/api/heatmap', methods=['POST'])
def heatmap():
    locations = request.json['locations']
    heatmap_url = generate_heatmap(locations)
    return jsonify({'heatmap_url': heatmap_url})

if __name__ == '__main__':
    app.run(debug=True)