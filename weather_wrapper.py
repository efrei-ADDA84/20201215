from flask import Flask, request, jsonify
from requests.exceptions import RequestException
import os
import requests

app = Flask(__name__)

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather_by_coordinates(self, latitude, longitude):
        complete_url = f"{self.base_url}lat={latitude}&lon={longitude}&appid={self.api_key}"
        try:
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
        except RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

api_key = os.environ.get("API_KEY")

if not api_key:
    raise ValueError("API_KEY environment variable is not set.")

weather_api = WeatherAPI(api_key)

@app.route('/weather', methods=['GET'])
def get_weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    if not latitude or not longitude:
        return jsonify({"error": "Latitude and longitude parameters are required."}), 400

    weather_data = weather_api.get_weather_by_coordinates(latitude, longitude)

    if weather_data:
        return jsonify(weather_data), 200
    else:
        return jsonify({"error": "Weather data not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
