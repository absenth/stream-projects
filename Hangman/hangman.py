import random
import os

# Set the list of words for the game & randomly select one.
wordlist = ["abyss","bubbly","buzz","buff","cozy","fluff","lucky","puzzle","hangman"]
gameword = random.choice (wordlist)

wordlen=len(gameword)
allletters = list(gameword)

# Gamestate variables
drawing=[
   """  ===|
  |
  |
  |
__|__ """,
"""  ===|
  |  O
  |
  |
__|_""",
"""  ===|
  |  O
  |  |
  |  |
__|_""",
"""  ===|
  |  O
  | /|
  |  |
__|_""",
"""  ===|
  |  O
  | /|\\
  |  |
__|_""",
"""  ===|
  |  O
  | /|\\
  |  |
__|_/""",
"""  ===|
  |  O
  | /|\\
  |  |
__|_/ \\"""]

# Game output set inital value
gameout = ["_"] * wordlen
gamestate = 0
guesses = []


while gamestate < 6:
    os.system('cls')
    print(drawing[gamestate])
    print("Your word has ", str(wordlen), " letters.")
    print(*gameout)
    print(*guesses)
    guess = input("Please enter your guess:").lower()[0]
    guesses.append(guess)
    changed = False
    for i,v in enumerate(allletters):
        if guess == v:
            changed = True
            gameout[i] = v
            print(*gameout)
    if changed == False:
        gamestate = gamestate +1
        print(*gameout)
    if "_" not in gameout:
        print(drawing[gamestate])
        print("You Win")
        exit()

print(drawing[6])
print("Stop Doing It Wrong!")

