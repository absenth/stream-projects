""" I have a friend in Sweden, and a Co-Worker in Berlin
    It would be super helpful to have a tool that trivially
    converted Celcius to Fahrenheit and back
    Formula is: C = (F - 32) / 1.8
"""


import re


def main():
    """Take user input, including a unit and convert it to it's partner unit"""

    print("Please Provide a Value and Unit to convert.")
    print("ie: 27c for celsius, or 75m for miles")
    user_value = input("> ")

    # validate that the user input a proper value
    if check_input(user_value):
        # detect the expecte conversion and execute
        value, unit = detect_unit(user_value)
        if unit == "c":
            temp = round(float(celsius_to_fahrenheit(value)), 2)
            print(f"Temperature is {temp} degrees Fahrenheit")
        elif unit == "f":
            temp = round(float(fahrenheit_to_celsius(value)), 2)
            print(f"Temperature is {temp} degrees Celcius")
        elif unit == "m":
            distance = round(float(miles_to_kilometers(value)), 2)
            print(f"Distance is {distance} kilometers")
        elif unit == "km":
            distance = round(float(kilometers_to_miles(value)), 2)
            print(f"Distance is {distance} miles")
        elif unit == "g":
            volume = round(float(gallons_to_liters(value)), 2)
            print(f"Volume is {volume} liters")
        elif unit == "l":
            volume = round(float(liters_to_gallons(value)), 2)
            print(f"Volume is {volume} gallons")
        elif unit == "p":
            weight = round(float(pounds_to_kilograms(value)), 2)
            print(f"Weight is {weight} kilograms")
        elif unit == "kg":
            weight = round(float(kilograms_to_pounds(value)), 2)
            print(f"Weight is {weight} pounds")
        else:
            invalid_input(user_value)


def check_input(input):
    if '.' in input:
        check = bool(re.match(r"^\d+\.\d+[a-zA-Z]$", input))
    else:
        check = bool(re.match(r"^\d+[a-zA-Z]$", input))
    if not check:
        invalid_input(input)
    return check


def detect_unit(input):
    """This function will read the user's input and determine
       which conversion function is needed"""
    m = re.search(r"^(?P<value>.+?)(?P<unit>[a-zA-Z]+)$", input)
    value = m.group('value')
    unit = m.group('unit').lower()
    return value, unit


def celsius_to_fahrenheit(input):
    """This function converts Celcius to Fahrenheit and returns"""
    temp = (float(input) * 1.8) + 32
    return temp


def fahrenheit_to_celsius(input):
    """This function converts Fahrenheit to Celcius and returns"""
    temp = (float(input) - 32) / 1.8
    return temp


def miles_to_kilometers(input):
    """This function converts Miles to Kilometers"""
    dist = float(input) * 1.609344
    return dist


def kilometers_to_miles(input):
    """This function converts Kilometers to Miles"""
    dist = float(input) / 1.609344
    return dist


def gallons_to_liters(input):
    """This function converts Gallons to Liters"""
    volume = float(input) / 0.26417
    return volume


def liters_to_gallons(input):
    """This function converts Liters to Gallons"""
    volume = float(input) * 0.26417
    return volume


def pounds_to_kilograms(input):
    """This function converts Pounds to Kilograms"""
    weight = float(input) * 0.44349237
    return weight


def kilograms_to_pounds(input):
    """This function converts Kilograms to Pounds"""
    weight = float(input) / 0.44349237
    return weight


def invalid_input(input):
    """This will print a help string for the user, and return them
       back to the main function to try again."""
    print(f"You input {input} which wasn't understood.")
    print("Please input a value like 27c")
    print("Units this program understands are:")
    print("c = celsius / f = fahrenheit / m = miles / km = kilometers")
    print("g = gallons / l = liters / p = poundsa / kg = kilograms")
    print("")

    main()


if __name__ == "__main__":
    main()
