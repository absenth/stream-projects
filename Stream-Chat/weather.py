import requests
import json
import os


def weather_lookup(city):
    city_name = city[0]
    api_key = os.getenv('OPENWEATHERMAP_API')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        celcius_temperature = current_temperature - 273.15
        fahrenheit_temperature = current_temperature * 1.8 - 459.67
        format_fahrenheit = "{:.2f}".format(fahrenheit_temperature)
        format_celcius = "{:.2f}".format(celcius_temperature)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        weather=(f"Temperature {format_celcius}c, {format_fahrenheit}f, Description = {weather_description}")
        return weather
    else:
        response="City Not Found"
        return response
