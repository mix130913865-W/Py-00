def parse_weather_data(data: dict) -> dict:
    """
    Extract relevant weather details from OpenWeatherMap API response JSON.

    Args:
        data (dict): JSON data returned by the API.

    Returns:
        dict: Extracted weather information including city, temperature, etc.
    """
    weather_info = {
        "city": data.get('name'),
        "temp": data['main'].get('temp'),
        "feels_like": data['main'].get('feels_like'),
        "temp_min": data['main'].get('temp_min'),
        "temp_max": data['main'].get('temp_max'),
        "description": data['weather'][0].get('description'),
        "humidity": data['main'].get('humidity'),
        "wind_speed": data['wind'].get('speed')
    }
    return weather_info
