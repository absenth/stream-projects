""" I have a friend in Sweden, and a Co-Worker in Berlin
    It would be super helpful to have a tool that trivially
    converted Celcius to Fahrenheit and back
    Formula is: C = (F - 32) / 1.8
"""


import re


def main():
    """Take a temperature as input and feed that to the conversion  function"""
    KnownTemperature = input("Input Temperature. ie:'27c' ")

    if CheckInput(KnownTemperature):
        ConvertedTemperature = ConvertTemp(KnownTemperature)
        Temp = ConvertedTemperature[0: -1]
        Unit = ConvertedTemperature[-1]
        Temp = float(Temp)
        Temp = round(Temp, 2)
        print(f"{Temp}{Unit}")


def ConvertTemp(input):
    """Take a temperature as input, and convert it"""
    if input[-1].lower() == "f":
        ConvertedTemperature = (float(input[0: -1]) - 32) / 1.8
        return(f"{ConvertedTemperature}c")
    elif input[-1].lower() == "c":
        ConvertedTemperature = (float(input[0: -1]) * 1.8) + 32
        return(f"{ConvertedTemperature}f")
    else:
        print("I can't convert your temperature without a unit")


def CheckInput(input):
    if '.' in input:
        check = bool(re.match(r"^\d+\.\d+[cCfF]$", input))
    else:
        check = bool(re.match(r"^\d+[cCfF]$", input))
    if check is False:
        print("The value you input didn't match the expected format. Please try again.")
        main()
    return check


if __name__ == "__main__":
    main()
