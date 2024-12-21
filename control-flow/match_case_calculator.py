#!/bin/bash
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition} ")
    case "-":
        subtract = num1 - num2
        print(f"The result is {subtract} ")
    case "*":
        multiply = num2 * num1
        print(f"The result is {multiply} ")
    case "/":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            divide = num1 / num2
            print(f"The result is {divide} ")



