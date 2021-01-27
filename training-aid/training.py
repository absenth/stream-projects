import os
import random

targets = [
        "A", "B", "C", "D", "E", 
        "1", "2", "3", "4", "5"
        ]

itteration = int(input("Please enter the number of itterations: "))

while itteration > 0:
  targetcount = random.randint(1, 5)
  while targetcount > 0:
    random_index = random.randrange(len(targets))
    os.system('echo "{0}" | festival --tts'.format(random_index)) 
    targetcount = targetcount - 1 
  input("Press Enter to continue... ")
  itteration = itteration - 1

