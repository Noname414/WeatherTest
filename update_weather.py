import requests
import json
import os
from datetime import datetime

def get_weather_data():
    api_key = os.environ.get('WEATHER_API_KEY')
    city = os.environ.get('CITY', 'Taipei')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_tw'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 添加時間戳
        data['timestamp'] = datetime.utcnow().isoformat()
        
        # 保存到文件
        with open('weather.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == '__main__':
    get_weather_data()