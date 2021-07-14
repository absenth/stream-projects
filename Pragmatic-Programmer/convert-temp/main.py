""" I have a friend in Sweden, and a Co-Worker in Berlin
    It would be super helpful to have a tool that trivially
    converted Celcius to Fahrenheit and back
    Formula is: C = (F - 32) / 1.8
"""

known_Temperature = input("Input Temperature.  ie:'27c' ")

if known_Temperature[-1].lower() == "f":
    converted_Temperature = (float(known_Temperature[0: -1]) - 32) / 1.8
    print(f"{known_Temperature} is {converted_Temperature}c")
elif known_Temperature[-1].lower() == "c":
    converted_Temperature = (float(known_Temperature[0: -1]) * 1.8) + 32
    print(f"{known_Temperature} is {converted_Temperature}f")
else:
    print("I can't convert your temperature without a unit")
