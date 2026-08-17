inventory = {}

while True:
    print("\n--- Inventory Manager ---")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = inventory.get(product, 0) + quantity

        print("Product added successfully.")

    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory")

            for product, quantity in inventory.items():
                print(f"{product}: {quantity}")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter quantity to add: "))
            inventory[product] += quantity
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product removed successfully.")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Exiting Inventory Manager.")
        break

    else:
        print("Invalid choice.")