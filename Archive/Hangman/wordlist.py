# wordlist.py
import random

wordlist = [
    "attempt", "border", "brick", "customs",
    "discussion", "essential", "exchange",
    "explanation", "fireplace", "floating",
    "garage", "grabbed", "grandmother",
    "heading", "independent", "instant",
    "manufacturing", "mathematics", "memory",
    "mysterious", "neighborhood", "occasionally",
    "official", "policeman", "positive",
    "possibly", "practical", "promised",
    "remarkable", "require", "satisfied",
    "scared", "selection", "shaking", "shallow",
    "simplest", "slight", "slope", "species",
    "thumb", "tobacco", "treated", "vessels",
    ]

def pickword():
    return random.choice (wordlist)

print(pickword())