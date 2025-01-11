#!/bin/bash
#Create an empty list.

shopping_list = []

#Define function to add items.

def add():
    item = input("Item to add: ")
    shopping_list.append(item)
    return(f"{item} has been added to the list.")
#result = add("item")
#print(f"{result}")

#Define function to remove items.

def remove():
    item = input("Item to remove: ")
    for item in shopping_list:
        shopping_list.remove(item)
        return(f"{item} has been removed")
    else:
        return(f"{item} not found on list")

#answer = remove("items")
#print(f"{answer}")


def display():
    if shopping_list:
        for item in shopping_list:
            return item
    else:
        return(f"the list is empty")
#output = display("items")
#print("output")


