#!/bin/bash
#Definiton of a function.

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
        if denominator == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
    except ValueError:
        return("Error: Please enter numeric values only.")
    else:
        return(f"The result of the division is {result:.1f}")


output = safe_divide(numerator=2, denominator=1)
print(f"{output}")
