# RollerCoaster

print("Welcome to the rollercoaster!")
# take the height input from the user and convert it to integer
height= int(input("Enter your  height in cm : "))
bill_amount=0  # initialize the bill amount to 0

if height>=120 : # check if the height is greater than or equal to 120 cm

    print("You can ride the rollercoaster!")

# if the user can ride the rollercoaster, take the age input from the user and convert it to integer
    age= int(input("Enter your age : "))

    if age<12 :
        bill_amount=5
        print(f"Your ticket price is ${bill_amount}.")
    elif age<=18 :
        bill_amount=7
        print(f"Your ticket price is ${bill_amount}.")
    else :
        bill_amount=12
        print(f"Your ticket price is ${bill_amount}.")
    # ask the user if they want to take a photo and store the answer in a variable
    want_photo= input("Do you want to take a photo? y or n : ")
    if want_photo == "y":
        bill_amount +=3 # if the user wants to take a photo, add 3 to the bill amount
        print(f"Your final bill amount is ${bill_amount}.")
    else:
        print(f"Your final bill amount is ${bill_amount}.")
# if the user cannot ride the rollercoaster, print a message
else :
    print("Sorry, you are too short to ride the rollercoaster.")