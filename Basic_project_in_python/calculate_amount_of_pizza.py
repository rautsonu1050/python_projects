# Practice Project : Calculating the amount of pizza to order
print("Welcome to Python pizza deliveries!")

# taking user input for pizza order
size = input("What size pizza do you want ? s , m or l :")
add_pepperoni = input("Do you want peppernoni ? y or n :")
extra_cheese = input("Do you want extra cheese ? y or n :")

bill_amount = 0  # initializing the bill amount variable to 0

# calculating the bill amount based on user input
if size == "s":
    bill_amount = 15

elif size == "m" :
    bill_amount= 20
    
else :
    bill_amount = 25

# adding the cost of pepperoni to the bill amount based on user input
if add_pepperoni == "y" and size == "s":
    bill_amount +=2 

elif add_pepperoni == "y" and size !="s" :
    bill_amount +=3

# adding the cost of extra cheese to the bill amount based on user input
if extra_cheese =="y" :
    bill_amount +=1

# printing the final bill amount and order details
print()
print("-------------------------------")
print("Your order details : ")
print(f"Pizza size : {size}")
print(f"Add pepperoni : {add_pepperoni}")
print(f"Extra cheese : {extra_cheese}")
print()
print(f"Your final bill amount is  ${bill_amount}.")
print("-------------------------------")