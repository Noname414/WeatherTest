import requests
import json
import os
from datetime import datetime

def get_weather_data():
    api_key = os.environ.get('WEATHER_API_KEY')
    city = os.environ.get('CITY', 'Taipei')
    
    if not api_key:
        print("Error: WEATHER_API_KEY is not set")
        raise ValueError("WEATHER_API_KEY is missing")
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_tw'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Verify that the response contains expected data
        if 'main' not in data or 'weather' not in data:
            print(f"Error: Invalid API response: {data}")
            raise ValueError("Invalid weather data received")
        
        # Add timestamp
        data['timestamp'] = datetime.utcnow().isoformat()
        
        # Save to file
        with open('weather.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Weather data successfully updated for {city} at {data['timestamp']}")
        
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        if response:
            print(f"Response content: {response.text}")
        raise
    
    except ValueError as e:
        print(f"Validation error: {e}")
        raise

if __name__ == '__main__':
    try:
        get_weather_data()
    except Exception as e:
        print(f"Script failed: {e}")
        exit(1)