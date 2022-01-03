import requests
import json
import os


def geocode_lookup(city):
    api_key = os.getenv('OPENCAGE_API_KEY')
    base_url = "http://api.opencagedata.com/geocode/v1/geojson?"
    complete_url = f"{base_url}&q={city}&key={api_key}&limit=1"
    response = requests.get(complete_url).json()
    coords = (response['features'][0]['geometry']['coordinates'])
    lat=coords[1]
    lng=coords[0]
    print(response['features'])
    return(lat,lng)


if __name__ == "__main__":
    lat,lng = geocode_lookup("austin")
    print(f"Lat: {lat}  Lng: {lng}")
