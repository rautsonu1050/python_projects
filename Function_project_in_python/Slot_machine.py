import random
import time

def spin_row():
    symbols = ['❤️', '👍', '🙌','😎']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '❤️':
            return bet * 3
        elif row[0] == '👍':
            return bet * 4
        elif row[0] == '🙌':
            return bet * 6
        elif row[0] == '😎':
            return bet * 10
    return 0

def main():
    balance = 5000
    print("Welcome to Python Slots!")

    while balance > 0:
        print(f"\nYour current balance: Rs. {balance}")

        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        balance -= bet  # Deduct bet first

        row = spin_row()
        print("Spinning...")
        time.sleep(0.5)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won Rs. {payout}!")
        else:
            print("Sorry! You lost this bet.")

        balance += payout  # Add winnings (if any)

        if balance <= 0:
            print("You ran out of money!")
            break

        play_again = input("Do you want to play again (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"\nGame over! Your final balance is: Rs. {balance}")

if __name__ == '__main__':
    main()