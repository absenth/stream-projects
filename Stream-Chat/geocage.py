import requests
import os


def geocode_lookup(city):
    api_key = os.getenv('OPENCAGE_API_KEY')
    base_url = "http://api.opencagedata.com/geocode/v1/geojson?"
    complete_url = f"{base_url}&q={city}&key={api_key}&limit=1"
    response = requests.get(complete_url).json()
    coords = (response['features'][0]['geometry']['coordinates'])
    utc_offset = (response['features'][0]['properties']['annotations']['timezone']['offset_string'])
    lat = coords[1]
    lng = coords[0]
    return lat, lng, utc_offset


if __name__ == "__main__":
    lat, lng, utc_offset = geocode_lookup("madrid")
    print(f"Lat: {lat}  Lng: {lng}  utc_offset: {utc_offset}")
