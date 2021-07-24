""" I have a friend in Sweden, and a Co-Worker in Berlin
    It would be super helpful to have a tool that trivially
    converted Celcius to Fahrenheit and back
    Formula is: C = (F - 32) / 1.8
"""


import re


def main():
    """Take user input, including a unit and convert it to it's partner unit"""

    print("Please Provide a Value and Unit to convert.")
    print("ie: 27c for celcius, or 75m for miles")
    UserValue = input("> ")
    CheckInput(UserValue)

    # Validate Input is Valid
    # Pass User Input to detect_Unit()
    # Call Function and pass the value
    # Present the returned Converted Value


def CheckInput(input):
    """This function will check for valid user input"""
    if '.' in input:
        check = bool(re.match(r"^\d+.\d+[a-zA-Z]{1,2}$", input))
    else:
        check = bool(re.match(r"^\d+[a-zA-Z{1,2}$", input))
    if check is False:
        InvalidInput(input)


def DetectUnit(input):
    """This function will read the user's input and determine
       which conversion function is needed"""
    if bool(re.match(^.*[a-zA-Z]{2}$", input)):
        # do pull the last two
        # return(conversion,value)
    else:
        # do pull the last one
        # return(conversion,value)


def CtoF():
    """This function converts Celcius to Fahrenheit and returns"""


def FtoC():
    """This function converts Fahrenheit to Celcius and returns"""


def MtoKM():
    """This function converts Miles to Kilometers"""


def KMtoM():
    """This function converts Kilometers to Miles"""


def GtoL():
    """This function converts Gallons to Liters"""


def LtoG():
    """This function converts Liters to Gallons"""


def PtoKG():
    """This function converts Pounds to Kilograms"""


def KGtoP():
    """This function converts Kilograms to Pounds"""


def InvalidInput(input):
    """This will print a help string for the user, and return them
       back to the main function to try again."""
