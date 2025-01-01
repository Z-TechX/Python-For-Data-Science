print("Welcome to the Shopping Cart Program!")

# Initialize variables
total_price = 0
item_count = 0

while True:
    # Ask user for the price of an item
    price = float(input("Enter the price of the item (or 0 to finish): "))
    
    # If the price is 0, exit the loop
    if price == 0:
        break
    
    # Add the price to the total
    total_price += price
    item_count += 1  # Count the item

# After the loop, print the total and item count
print("\nShopping Summary:")
print("Total number of items:", item_count)
print("Total price: $", total_price)
