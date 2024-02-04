import asyncio
import python_weather

async def get_weather_conditions(city_name):
    # Create an asynchronous context for the python_weather client
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        # Fetch weather information for the given city name
        weather = await client.find(city_name)
        
        # Extract and return relevant weather information from the response
        return {
            "temperature": weather.current.temperature,
            "visibility": weather.current.visibility
        }
    
 
