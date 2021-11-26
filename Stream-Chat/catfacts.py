import urllib
import requests
import json

def cat_fact():
    base_url = "https://catfact.ninja/fact"
    response = requests.get(base_url)
    x = response.json()
    returned_fact = x["fact"]

    return(returned_fact)
