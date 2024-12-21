#!/bin/bash
#Enter a number
number = int(input("Enter a number to see its multiplication table: "))


i = 0
for i in (1,2,3,4,5,6,7,8,9,10):
            product = number * i
            print(f"{number} * {i} = {product}" )
