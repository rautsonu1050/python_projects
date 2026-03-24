def show_balance(balance):
    print("*" *30)
    print(f"Your Balance amount is Rs.{balance :.2f}")
    print()
    print("*" *30)
    
def deposite():
    amount = float(input("Enter amount to be deposite :"))
    if amount <0 :
        print("That is not valid amount ")
        return 0 
    return amount
def withdraw(balance):
    amount = float(input("Enter amount to be withdraw : "))
    if amount > balance :
        print("Insufficient Balance ")
    elif amount < 0 :
        print("Invaild amount ")
    else:
        return amount
def main():
    balcnce= 500
    is_running=True
    while is_running:
        print("Banking Program ")
        print("1.Show Balance")
        print("2.Deposite")
        print("3.Withdraw")
        print("4.Exit")
        choice =input("Enter your choice (1-4) : ")
        if choice == "1":
            show_balance(balcnce)
            print()
        elif choice == "2":
            balcnce+=deposite()
            print("*" *30)
            print(f"Your new balance is : {balcnce}")
            print()
            print("*" *30)
            
        elif choice =="3":
            balcnce-=withdraw(balcnce)
            print("*" *30)
            print(f"Your have Rs. {balcnce} balance left in your bank ")
            print()
            print("*" *30)
        elif choice =="4":
            is_running= False
        else:
            print ("Invalid choice! ")
    print("*" *30)
    print("Thank you ! Have a nice day")
    print("*" *30)
main()




