""" I have a friend in Sweden, and a Co-Worker in Berlin
    It would be super helpful to have a tool that trivially
    converted Celcius to Fahrenheit and back
    Formula is: C = (F - 32) / 1.8
"""

def main():
    """Take a temperature as input and feed that to the conversion  function"""
    known_Temperature = input("Input Temperature. ie:'27c' ")

    converted_Temperature = convert_Temp(known_Temperature)
    print(converted_Temperature)

def convert_Temp(temp_Input):
    """Take a temperature as input, and convert it"""
    if temp_Input[-1].lower() == "f":
        converted_Temperature = (float(temp_Input[0: -1]) - 32) / 1.8
        return(f"{converted_Temperature}c")
    elif temp_Input[-1].lower() == "c":
        converted_Temperature = (float(temp_Input[0: -1]) * 1.8) + 32
        return(f"{converted_Temperature}f")
    else:
        print("I can't convert your temperature without a unit")


if __name__ == "__main__":
    main()