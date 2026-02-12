# Hotel Menu 


# Dictionary to store food items and their prices
menu = {
        "pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "soda": 3.50
        }


# List to store ordered items
cart=[]

# Variable to store total bill amount
total = 0

# Display menu heading
print("\n      MENU          \n")

# Display all menu items with prices
for key,value in menu.items():
  print (f"{key:10} ${value:.2f}")

while True:
    # Take item input from user

  food =input("Select items you want (q to quite) : ").lower()

  if food=="q":     # If user enters 'q', stop ordering
    break
  
    # If item is available in menu, add to cart
  elif food in menu:
    cart.append(food)

  else:     # If item not found in menu, display message
    print("Items not availabel!")

# Display order summary
print("\n\n-------YOYR ORDER-------")
for food in cart:
    # Print item name and its price
  print (f"{food:10} ${menu[food]:.2f}")

  total+=menu[food]


# Print total bill
print("-------------------------")
print(f"Total is    ${total:.2f}")
print("--------------------------")

