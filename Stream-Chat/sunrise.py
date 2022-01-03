import requests
import json
import os


def sunrise_lookup(lat,lng):
    base_url = "https://api.sunrise-sunset.org/json?"
    complete_url = base_url + "lat=" + lat + "&lng=" + lng

    # Example QUERY string
    # https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
    # https://api.sunrise-sunset.org/json?lat=-97.7436995&lng=30.2711286

    response = requests.get(complete_url).json()
    print(complete_url)
    print(response)


if __name__ == "__main__":
    sunrise_lookup("-97.7436995", "30.2711286")
