import requests

# Input OpenWeatherMap API key
API_KEY = "a7aed2194e1f40e6f487d88b749d29d0"


def get_weather(city_name):
    # API endpoint URL for current weather data
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters to send in the API request
    params = {
        "q": city_name,        # City name, e.g., "Taipei"
        "appid": API_KEY,      # Your API key for authentication
        "units": "metric",     # Use metric units (Celsius)
        "lang": "en"           # Response language in English
    }

    # Send GET request to the weather API with parameters
    response = requests.get(url, params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response body
        data = response.json()

        # Extract relevant weather information from JSON
        city = data['name']
        temp = data['main']['temp']                  # Current temperature
        feels_like = data['main']['feels_like']      # Feels like temperature
        temp_min = data['main']['temp_min']          # Minimum temperature
        temp_max = data['main']['temp_max']          # Maximum temperature
        # Weather condition description
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']          # Humidity percentage
        wind_speed = data['wind']['speed']           # Wind speed in m/s

        # Print the weather information nicely formatted
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Minimum Temperature: {temp_min} °C")
        print(f"Maximum Temperature: {temp_max} °C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        # If the response code is not 200, print an error message
        print("Warning: Failed to get weather data. Please check the city name.")


if __name__ == "__main__":
    # Prompt user to input city name
    city = input("Enter city name: ")

    # Call the function to get and display weather info
    get_weather(city)
