import math

print("Welcome to the online banking application")

# Function to create a new user account
def signin():
    global name  # username
    global pin  # password
    name = input("Please create your username: ")
    pin = input("Please create your 6-digit pin: ")
    while len(pin) != 6 or not pin.isdigit():
        print("Invalid pin. Pin must be 6 digits.")
        pin = input("Please create your 6-digit pin: ")
    print("Thanks for creating your bank account")

# Function for the user to recover the pin
def forgotpin():
    global pin
    recoverpin = input("Please create your new 6-digit pin: ")
    while len(recoverpin) != 6 or not recoverpin.isdigit():
        print("Invalid pin. Pin must be 6 digits.")
        recoverpin = input("Please create your new 6-digit pin: ")
    print("The new pin has been stored, please log in")
    pin = recoverpin

# Function to calculate deposit interest
def depositinterest(p, r, t):
    return p * math.exp(r * t)

# Function for user login
def login():
    global cb  # current balance
    name1 = input("Please enter your username: ")
    pin1 = input("Please enter your pin: ")
    if name1 == name and pin1 == pin:
        print("Welcome to the online banking application, " + name)
        print("Options:")
        print("1-Deposit\n2-Withdraw\n3-Transfer\n4-Check Balance\n5-Deposit interest rate\n6-Calculate compound interest")
        choice = input("Enter the number of your choice: ")

        if choice == '1':  # Deposit money
            try:
                amount = int(input("Enter the amount you want to deposit: "))
                cb += amount
                print("Deposit successful. Your current balance is: " + str(cb))
            except ValueError:
                print("Invalid input. Amount must be a number.")
        elif choice == '2':  # Withdraw money
            try:
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount > cb:
                    print("Insufficient funds for withdrawal.")
                else:
                    cb -= amount
                    print("Withdrawal successful. Your current balance is: " + str(cb))
            except ValueError:
                print("Invalid input. Amount must be a number.")
        elif choice == '3':  # Transfer money
            dest = input("Enter the 8-digit account number for the transfer: ")
            try:
                amount = int(input("Enter the amount you want to transfer: "))
                if amount > cb:
                    print("Insufficient funds for transfer.")
                else:
                    cb -= amount
                    print("Transfer successful. Your current balance is: " + str(cb))
            except ValueError:
                print("Invalid input. Amount must be a number.")
        elif choice == '4':  # Check balance
            print("Your current balance is: " + str(cb))
        elif choice == '5':  # Deposit interest rate
            try:
                r = float(input("Enter the interest rate: "))
                t = float(input("Enter the time period: "))
                print("The future value of your investment is: ", depositinterest(cb, r, t))
            except ValueError:
                print("Invalid input. Rate and time must be numbers.")
        elif choice == '6':  # Calculate compound interest
            try:
                p = float(input("Enter the principal amount: "))
                r = float(input("Enter the interest rate: "))
                t = float(input("Enter the time period: "))
                print("The compound interest is: ", depositinterest(p, r, t))
            except ValueError:
                print("Invalid input. Principal, rate and time must be numbers.")
        print("Thank you for using the online banking application.")
    else:
        print("Incorrect username or pin. Have you created your account?")
        choice = input("Enter your choice: 1- Yes, 2- No")

        if choice == '1':
            choice2 = input("Do you want to attempt to log in again? 1- Yes, 2- Forgot your pin")
            if choice2 == '1':
                login()
            elif choice2 == '2':
                forgotpin()
            else:
                print("Option is not available")
                login()
        elif choice == '2':
            print("Please create your account")
            signin()

cb = 0
signin()
login()
