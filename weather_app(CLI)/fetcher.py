import requests

# OpenWeatherMap API key (replace with your own key if needed)
API_KEY = "a7aed2194e1f40e6f487d88b749d29d0"

def fetch_weather_json(city_name: str) -> dict | None:
    """
    Fetch raw weather data JSON from OpenWeatherMap API for a given city.

    Args:
        city_name (str): Name of the city to query.

    Returns:
        dict: Parsed JSON data if request successful.
        None: If request failed.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    