import IPython


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
            # Prompt for and add “
            IPython
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
            item = input("Enter item to add: ").strip()
            if item:  # Check if input is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item name cannot be empty.")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        print()  # Empty line for better readability

if __name__ == "__main__":
    main()