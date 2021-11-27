import urllib
import requests
import json

def cat_fact():
    return requests.get('https://catfact.ninja/fact').json()['fact']
