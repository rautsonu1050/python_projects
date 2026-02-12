# Password Validation : 

# number of login attempts allowed
attempt = 3

# taking username input from user
username= input("Enter your user name: ")

#loop will run until the  attempts become 0
while attempt > 0:
    
    # checking if the username is correct
    if username =="admin":
        
        # taking password input from user

        password = input("Enter your password :")

        # checking if the password is correct Login successful
        if password== "python123":
          print("Successfully login")
          
          break # exit the loop if login is successful
        else:
         
         # if password is wrong then decrease the attempts by 1 and print the remaining attempts  
         attempt-=1
         print(f"Worng password .{attempt} attemptes left!")
          
    else:
      # if username is incorrect 

      print("\nUser not found!")
      print()
      print(" Please visit to the nearest bank. ")
      print("            Thank You!            ")
      break # exit the loop if username is incorrect


# if attempts become 0 then print account locked message
if attempt == 0:
   print()
   print("          Account Locked             ")
   print(" Please visit to the nearest bank.    ")
 
   print("            Thank You!            ")