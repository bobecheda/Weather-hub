import os
import requests
from typing import Dict, Any, Optional
from django.conf import settings

class WeatherAPI:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError('OpenWeatherMap API key not found in environment variables')
    
    def get_weather_by_city(self, city: str) -> Dict[str, Any]:
        """Fetch weather data for a given city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use metric units (Celsius, meters/sec)
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return self._process_weather_data(response.json())
        except requests.RequestException as e:
            raise WeatherAPIError(f'Error fetching weather data: {str(e)}')
    
    def _process_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the raw API response into a more usable format."""
        try:
            return {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        except KeyError as e:
            raise WeatherAPIError(f'Invalid weather data format: {str(e)}')

class WeatherAPIError(Exception):
    """Custom exception for weather API related errors."""
    pass