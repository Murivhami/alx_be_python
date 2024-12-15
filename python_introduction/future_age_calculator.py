#!/bin/bash
#Python script that asks the user for their current age and then calculates how
# old they will be in a specific future year.
user_age = int(input("How old are you?"))
current_year = 2023

# Calculate users age in 2050
result = 2050 - current_year + user_age
print(f"In 2050, you will be {result} years old ")

