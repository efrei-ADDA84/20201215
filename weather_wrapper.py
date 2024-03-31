import requests
import os

def get_weather_by_coordinates(latitude, longitude, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]

        temp = main_data["temp"] - 273.15
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]

        return {
            "temperature": temp,
            "pressure": pressure,
            "humidity": humidity,
            "description": description
        }
    else:
        return None

api_key = os.environ.get("API_KEY")
latitude = float(os.environ.get("LAT"))
longitude = float(os.environ.get("LONG"))

if api_key and latitude and longitude:
    weather_data = get_weather_by_coordinates(latitude, longitude, api_key)
    if weather_data:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Pression: {weather_data['pressure']} hPa")
        print(f"Humidité: {weather_data['humidity']}%")
        print(f"Météo: {weather_data['description']}")
    else:
        print("Error: Weather data not found.")
else:
    print("Error: Missing API_KEY, LAT or LONG environment variables.")
