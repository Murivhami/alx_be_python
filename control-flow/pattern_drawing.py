#!/bin/bash
positive_integer = int(input("Enter the size of the pattern: "))

i = 0

while i < positive_integer:
    j = 0
    while j < positive_integer:
        print("*", end="")
        j += 1
    print()
    i += 1
