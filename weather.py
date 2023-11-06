import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from dataclasses import dataclass
@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


load_dotenv()
api_key = os.getenv('API_KEY')

def get_lat_lon(city_name, state_code, country_code, API_key):
    respLat = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    respLon = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data1 = respLat[0]
    data2 = respLon[0]
    lat, lon = data1.get('lat'), data2.get('lon')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperature = int(resp.get('main').get('temp'))
    )

    return data

def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    WeatherData = get_current_weather(lat, lon, api_key)
    return WeatherData

if __name__ == "__main__" :
    lat, lon = get_lat_lon('vijayawada', 'AP', 'India', api_key)
    print(get_current_weather(lat, lon, api_key))
