from fetcher import fetch_weather_json
from parser import parse_weather_data

def display_weather_info(info: dict):
    """
    Nicely print weather information to the console.

    Args:
        info (dict): Weather info dictionary extracted from API response.
    """
    print(f"\nWeather in {info['city']}:")
    print(f"Temperature: {info['temp']} °C")
    print(f"Feels Like: {info['feels_like']} °C")
    print(f"Minimum Temperature: {info['temp_min']} °C")
    print(f"Maximum Temperature: {info['temp_max']} °C")
    print(f"Condition: {info['description']}")
    print(f"Humidity: {info['humidity']}%")
    print(f"Wind Speed: {info['wind_speed']} m/s")

def main():
    city = input("Enter city name: ")
    data = fetch_weather_json(city)
    if data:
        info = parse_weather_data(data)
        display_weather_info(info)
    else:
        print("Warning: Failed to get weather data. Please check the city name.")

if __name__ == "__main__":
    main()
