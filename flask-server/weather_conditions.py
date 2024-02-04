import asyncio
import python_weather

async def get_weather_conditions(city_name):
    # Create an asynchronous context for the python_weather client
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        # Fetch weather information for the given city name
        weather = await client.find(city_name)
        
        # Extract and return relevant weather information from the response
        visibility = weather.current.visibility
        print(f"Visibility in NYC: {visibility} meters")
        return visibility
    
 
