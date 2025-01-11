#!/bin/bash
import datetime
# Create a function

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

current_date = display_current_datetime()
formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted_datetime}")

import datetime
#Calculate future date.
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    current_date = datetime.datetime.now()
    tdelta = datetime.timedelta(days = number_of_days)
    future_date = current_date + tdelta
    return future_date

future_date = calculate_future_date()
formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Future date: {formatted_future_date}")
