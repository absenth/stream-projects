import urllib
import requests
import json

def norris_joke():
    return requests.get('https://api.chucknorris.io/jokes/random?category=dev').json()['value']
