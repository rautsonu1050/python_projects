class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    def check_balance(self):
        return self._balance


# create account
name = input("Enter your name: ")
balance = int(input("Enter initial balance: "))
user = BankAccount(name, balance)

# menu
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        user.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        user.withdraw(amount)

    elif choice == "3":
        print("Your total balance Rs.", user.check_balance())

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")