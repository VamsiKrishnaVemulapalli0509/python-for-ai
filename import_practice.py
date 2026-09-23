import requests

# We need coordinates to get weather data
latitude = 16.44 # yanam latitude
longitude = 82.13   # yanam longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&timezone=Asia/Kolkata"

# Make the request
response = requests.get(url)
data = response.json()

print(data)