import os

import requests
import json
from dotenv import load_dotenv


def get_weather(city):
    load_dotenv()
    weather_token = os.getenv("WEATHER_TOKEN")
    weather_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
    response = requests.get(weather_link).json()
    description = response['weather'][0]['description']
    temperature = round(response['main']['temp'] - 273)
    humidity = response['main']['humidity']
    weather = f'Weather description - {description}\nTemperature - {temperature} C\nHumidity - {humidity}%'
    return weather
