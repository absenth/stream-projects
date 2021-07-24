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
    user_value = input("> ")
    check_input(user_value)

    # Validate Input is Valid
    # Pass User Input to detect_Unit()
    # Call Function and pass the value
    # Present the returned Converted Value


def check_input(input):
    """This function will check for valid user input"""
    if '.' in input:
        check = bool(re.match(r"^\d+.\d+[a-zA-Z]{1,2}$", input))
    else:
        check = bool(re.match(r"^\d+[a-zA-Z{1,2}$", input))
    if check is False:
        invalid_input(input)


def detect_unit(input):
    """This function will read the user's input and determine
       which conversion function is needed"""
    if bool(re.match(r"^.*[a-zA-Z]{2}$", input)):
        unit = input[-2].lower()
        value = input[0: -2]
        switch (unit) {
            case km: conversion = "km2m";
                     break;
            case kg: conversion = "kg2g";
                     break;
        return(conversion,value)
    else:
        unit = input[-1].lower()
        value = input[0: -1]
        switch (unit) {
            case c: conversion = "c2f";
                    break;
            case f: conversion = "f2c";
                    break;
            case m: conversion = "m2km";
                    break;
            case g: conversion = "g2l";
                    break;
            case l: conversion = "l2g";
                    break;
            case p: conversion = "p2kg";
                    break;
        return(conversion,value)


def c2f():
    """This function converts Celcius to Fahrenheit and returns"""


def f2c():
    """This function converts Fahrenheit to Celcius and returns"""


def m2km():
    """This function converts Miles to Kilometers"""


def km2m():
    """This function converts Kilometers to Miles"""


def g2l():
    """This function converts Gallons to Liters"""


def l2g():
    """This function converts Liters to Gallons"""


def p2kg():
    """This function converts Pounds to Kilograms"""


def kg2p():
    """This function converts Kilograms to Pounds"""


def invalid_input(input):
    """This will print a help string for the user, and return them
       back to the main function to try again."""
