inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

# Ask the user to enter an item
item = input("Enter item name: ").lower()

# Check if the item exists
if item in inventory:
    sold = int(input("How many items were sold? "))

    # Decrease the quantity
    inventory[item] -= sold

    # Remove the item if quantity becomes 0
    if inventory[item] == 0:
        del inventory[item]

    print("\nUpdated Inventory:")
    print(inventory)

else:
    print("Item not found in inventory.")