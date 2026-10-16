
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("===== INVENTORY CONTROL SYSTEM =====")

while True:
    
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except:
        print("Invalid input! Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        if inventory:
            print("--- Current Inventory ---")

            for i, item in enumerate(inventory, start=1):
                print(f"{i}{item}")
        else:
            print("Inventory is empty.")

    elif choice == 2:

        item = input("Enter item name to add: ").strip()

        if not item:

            print("Item name cannot be empty")
        elif item in inventory:

            print("Item already exists in inventory")
        else:
            inventory.append(item)

            print(f"'{item}' added to inventory.")

    elif choice == 3:
        item = input("Enter item name to remove: ").strip()

        if item in inventory:

            inventory.remove(item)
            print(f"'{item}' removed from inventory")
        else:
            print(f"'{item}' not found in inventory")

    elif choice == 4:
        inventory.sort()
        print("Inventory sorted alphabetically:")

        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

    elif choice == 5:

        print("Thank you for using Inventory Control System!")
        break

    else:
        print("Invalid choice! Please select a number from 1 to 5")
