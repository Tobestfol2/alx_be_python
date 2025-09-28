# shopping_list_manager.py: A simple script to manage a shopping list using a Python list.

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("-----------------------------")

def main():
    """Main function to run the shopping list application."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add.capitalize())
                print(f"'{item_to_add.capitalize()}' has been added to the list.")
            else:
                print("Item cannot be empty.")
                
        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove:
                # Use a try-except block to handle case where item is not found
                try:
                    shopping_list.remove(item_to_remove.capitalize())
                    print(f"'{item_to_remove.capitalize()}' has been removed from the list.")
                except ValueError:
                    print(f"'{item_to_remove.capitalize()}' was not found in the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '3':
            # 3. View List
            print("\n--- Your Shopping List ---")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is currently empty.")
            print("--------------------------")
            
        elif choice == '4':
            # 4. Exit
            print("Goodbye! Happy shopping.")
            break
            
        else:
            # Handle invalid choice
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
