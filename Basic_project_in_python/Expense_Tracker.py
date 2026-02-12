# Create your personal expense tracker in Python. The program should allow you to add expenses, view your total expenses

# Expense Tracker Project

expenses = [] # List of expenses in the form of dictionaries

print("\n--------Welcome to the Expense Tracker!--------")

while True:
    print("\nPlease select an option:")
    print("1. Add an expense")
    print("2. View All expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Add an expense
        try:
            date = input("Enter the date of the expense (YYYY-MM-DD): ")
            amount = float(input("Enter the amount of the expense: "))
            category = input("Enter the category of the expense (e.g., Food, Transport, etc.): ")

            expenses.append({'date': date,
                            'amount': amount,
                            'category': category})
            
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
    
    elif choice == '2':
        # View all expenses
        if expenses:
            print("\n All Expenses:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. Date: {expense['date']}, Amount: Rs.{expense['amount']:.2f}, Category: {expense['category']}")
        else:
            print("No expenses recorded yet.")
    
    elif choice == '3':
        # View total expenses
        total_expenses = 0
        for expense in expenses:
            total_expenses += expense['amount']
        print(f"Total expenses: Rs.{total_expenses:.2f}")
    
    elif choice == '4':
        # Exit the program
        print("Thank you for using the Expense Tracker! Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")