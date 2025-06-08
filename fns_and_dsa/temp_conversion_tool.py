FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = input("Enter the temperature to convert: ")
if temp.isnumeric():
    temp = float(temp)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit == "C" or unit == "c":
        print(temp,"°C is", convert_to_fahrenheit(temp), "°F")
    elif unit == "F" or unit == "f":
        print(temp,"°F is", convert_to_celsius(temp), "°C")
    else:
        print("This is not supported unit")
else:
    print("Invalid temperature. Please enter a numeric value.")

