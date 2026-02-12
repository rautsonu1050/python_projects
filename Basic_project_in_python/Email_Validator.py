
# Simple Email Validator project in Python

#Tkae input as email from user
email = input("Enter email: ")

# Validate email
if "@" in email and "." in email.split("@")[1]:

    # Split the email into username and domain
    username = email.split("@")[0]
    domain = email.split("@")[1]

    # Print the results
    print(f"Valid email!")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    # If the email is not valid, print an error message
    print("Invalid email format")