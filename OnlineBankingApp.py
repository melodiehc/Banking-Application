import math

print("Welcome to the Online Banking Application")

# Global variables
name = ""
pin = ""
cb = 0  # Current balance


# Function to create a new user account
def signin():
    global name, pin
    name = input("Please create your username: ")
    pin = input("Please create your 6-digit pin: ")
    while len(pin) != 6 or not pin.isdigit():
        print("Invalid pin. Pin must be 6 digits.")
        pin = input("Please create your 6-digit pin: ")
    print("Thank you for creating your bank account.")


# Function to recover the pin
def forgotpin():
    global pin
    recoverpin = input("Please create your new 6-digit pin: ")
    while len(recoverpin) != 6 or not recoverpin.isdigit():
        print("Invalid pin. Pin must be 6 digits.")
        recoverpin = input("Please create your new 6-digit pin: ")
    print("Your new pin has been stored. Please log in again.")
    pin = recoverpin


# Function to calculate deposit interest
def depositinterest(p, r, t):
    return p * math.exp(r * t)


# Function for user login
def login():
    global cb
    name1 = input("Please enter your username: ")
    pin1 = input("Please enter your pin: ")

    if name1 == name and pin1 == pin:
        print(f"Welcome to the Online Banking Application, {name}.")
        while True:
            print("\nOptions:")
            print("1 - Deposit")
            print("2 - Withdraw")
            print("3 - Transfer")
            print("4 - Check Balance")
            print("5 - Deposit Interest Rate")
            print("6 - Calculate Compound Interest")
            print("7 - Exit")
            choice = input("Enter the number of your choice: ")

            if choice == '1':  # Deposit money
                try:
                    amount = int(input("Enter the amount you want to deposit: "))
                    cb += amount
                    print(f"Deposit successful. Your current balance is: {cb}")
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '2':  # Withdraw money
                try:
                    amount = int(input("Enter the amount you want to withdraw: "))
                    if amount > cb:
                        print("Insufficient funds for withdrawal.")
                    else:
                        cb -= amount
                        print(f"Withdrawal successful. Your current balance is: {cb}")
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '3':  # Transfer money
                dest = input("Enter the 8-digit account number for the transfer: ")
                if len(dest) != 8 or not dest.isdigit():
                    print("Invalid account number. Must be 8 digits.")
                    continue
                try:
                    amount = int(input("Enter the amount you want to transfer: "))
                    if amount > cb:
                        print("Insufficient funds for transfer.")
                    else:
                        cb -= amount
                        print(f"Transfer successful. Your current balance is: {cb}")
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '4':  # Check balance
                print(f"Your current balance is: {cb}")
            elif choice == '5':  # Deposit interest rate
                try:
                    r = float(input("Enter the annual interest rate (as a decimal): "))
                    t = float(input("Enter the time period in years: "))
                    print(f"The future value of your investment is: {depositinterest(cb, r, t):.2f}")
                except ValueError:
                    print("Invalid input. Rate and time must be numbers.")
            elif choice == '6':  # Calculate compound interest
                try:
                    p = float(input("Enter the principal amount: "))
                    r = float(input("Enter the annual interest rate (as a decimal): "))
                    t = float(input("Enter the time period in years: "))
                    print(f"The compound interest is: {depositinterest(p, r, t):.2f}")
                except ValueError:
                    print("Invalid input. Principal, rate, and time must be numbers.")
            elif choice == '7':  # Exit
                print("Thank you for using the Online Banking Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect username or pin.")
        choice = input("Do you want to recover your pin? (yes/no): ").strip().lower()
        if choice == 'yes':
            forgotpin()
            login()
        elif choice == 'no':
            print("Please create a new account.")
            signin()
            login()
        else:
            print("Invalid input. Returning to main menu.")
            login()


# Main program flow
signin()
login()
