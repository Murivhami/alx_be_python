#!/bin/bash
#Define functions to convert temperatures between Celsius and Fahrenheit.

#1. Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


#2. Implement Conversion Functions:

def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit == "C":
         converted = convert_to_fahrenheit(temperature)
         return(f"{temperature}°C is {converted}°F")

        elif unit == "F":
            converted = convert_to_celsius(temperature)
            return(f"{temperature}°F is {converted}°C")

        else:
            return("Invalid unit")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "_main_":
    main()
