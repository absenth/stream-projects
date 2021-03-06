import os
from drawing import gallows
from wordlist import pickword

# Set the list of words for the game & randomly select one.
gameword = pickword()

wordlen=len(gameword)
allletters = list(gameword)

# Game output set inital value
gameout = ["_"] * wordlen
gamestate = 0
guesses = []

while gamestate < 6:
    os.system('cls')
    gallows(gamestate)
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
        gallows(gamestate)
        print("You Win")
        exit()

gallows(6)
print("Stop Doing It Wrong!")
print("Your word was", gameword)
