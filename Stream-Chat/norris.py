import requests

def norris_joke():
    return requests.get('https://api.chucknorris.io/jokes/random?category=dev').json()['value']
