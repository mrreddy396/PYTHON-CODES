# weather_api.py
import requests


class WeatherAPI:
    def get_weather(self, city):
        url = f"https://api.example.com/weather/{city}"
        response = requests.get(url)
        return response.json()