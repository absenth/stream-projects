import os
import random
import time

targets = [
        "A", "B", "C", "D", "E", 
        "1", "2", "3", "4", "5"
        ]

itteration = int(input("Please enter the number of itterations: "))

while itteration > 0:
  targetcount = random.randint(1, 5)
  input("press enter when ready")
  while targetcount > 0:
    random_index = random.randrange(len(targets))
    os.system('echo "{0}" | festival --tts'.format(random_index)) 
    targetcount = targetcount - 1 
  itteration = itteration - 1

