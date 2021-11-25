import urllib
import requests
import json

def norris_joke():
    base_url = "https://api.chucknorris.io/jokes/random?category=dev"
    response = requests.get(base_url)
    x = response.json()
    joke = x["value"]

    return(joke)
