#!/bin/bash
positive_integer = int(input("Enter the size of the pattern: "))

for i in range(positive_integer):
    for j in range(positive_integer):
        print("*", end="")
    print()
