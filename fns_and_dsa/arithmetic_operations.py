#!/bin/bash
# Creating a function to perform arithmetic operations,

def perform_operation():
    #define type
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        #retrun a result for division by zero.
        if num2 == 0.0:
            return "Division by zero not possible"
        return num1 / num2

result = perform_operation()
print(f"{result}")
