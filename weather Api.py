# import requests

# # We need coordinates to get weather data
# latitude = 16.44 # yanam latitude
# longitude = 82.13   # yanam longitude

# # Build the API URL with our parameters
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&timezone=Asia/Kolkata"

# # Make the request
# response = requests.get(url)
# data = response.json()

# print(data)


import requests


def fetch_weather_data(latitude: float, longitude: float) -> dict:

    """Fetches real-time weather data from Open-Meteo API for given coordinates."""

    endpoint_url = "https://api.open-meteo.com/v1/forecast"

    params = {

        "latitude": latitude,

        "longitude": longitude,

        "current_weather": "true",

    }

    response = requests.get(endpoint_url, params=params, timeout=10)

    print(f"Request URL: {response.url}")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:

        data = response.json()

        temperature = data["current_weather"]["temperature"]

        print(f"Current Temperature: {temperature}°C")

        return data

    else:

        print(f"API Request Failed with Status Code: {response.status_code}")

        return {}


if __name__ == "__main__":

    # Test locations

    locations = [

        {"name": "New York", "lat": 40.7128, "lon": -74.0060},

        {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},

        {"name": "London", "lat": 51.5074, "lon": -0.1278},

    ]

    for loc in locations:

        print(f"\n--- Fetching weather for {loc['name']} ---")

        fetch_weather_data(loc["lat"], loc["lon"])
