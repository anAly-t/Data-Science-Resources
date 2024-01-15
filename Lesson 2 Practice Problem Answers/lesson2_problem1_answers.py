# DASC1092 Lesson 2 Problem 1

# Practice Assignment 1: Shopping List Operations

def shopping_list_manager():
    # Initialize an empty list to store shopping items
    shopping_list = []

    # Infinite loop for the shopping list manager
    while True:
        # Display the available shopping list operations
        print("\nShopping List Operations:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display list")
        print("4. Check if item exists")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        # Check user's choice and perform corresponding operation
        if choice == '1':
            # Add item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")

        elif choice == '2':
            # Remove item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
            # Display the current shopping list
            print("\nCurrent Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

        elif choice == '4':
            # Check if a specific item exists in the shopping list
            item = input("Enter the item to check: ")
            if item in shopping_list:
                print(f"{item} is in the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")

        elif choice == '5':
            # Exit the shopping list manager
            print("Exiting the Shopping List Manager.")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    # Call the shopping_list_manager function when the script is run
    shopping_list_manager()
