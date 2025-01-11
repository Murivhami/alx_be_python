#!/bin/bash
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Item to add: ")
            shopping_list.append(item)
            return(f"{item} has been added to the list.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                return(f"{item} has been removed")
            else:
                return(f"'{item}' was not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                return(f"Shopping list: ")
            else:
                return(f"Shopping list is empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
