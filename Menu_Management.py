menu_items = []
def add(item):
    global menu_items
    menu_items.append(item)
    print("After item added, the updated menu is:", menu_items)

def remove(item):
    global menu_items
    if item in menu_items:
        menu_items.remove(item)
        print("After item removed, the updated menu is:", menu_items)
    else:
        print(f"Item '{item}' not found in the menu.")

def check_item(item):
    if item in menu_items:
        print(f"Availability: {item} is available.")
    else:
        print(f"Availability: {item} is not available.")

def display():
    while True:
        print("\nMenu Management :")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Check if an item is available")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_to_add = input("Enter item to add: ")
            add(item_to_add)
        elif choice == 2:
            item_to_remove = input("Enter item to remove: ")
            remove(item_to_remove)
        elif choice == 3:
            item_to_check = input("Enter item to check: ")
            check_item(item_to_check)
        elif choice == 4:
            print("Exiting from the menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

menu_items = eval(input("Enter items in the menu list : "))
display()
