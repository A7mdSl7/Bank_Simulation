# Welcome  Print a simple random bank name

# Account Creation:
# Ask for the user’s name and initial balance.

# Main Menu (Loop):
# 1: Check balance → show balance.
# 2: Deposit → ask amount, add to balance.
# 3: Withdraw → ask amount, subtract if enough balance, else warn.
# 4: Exit → end program with a thank-you message.

# Details:
# Use functions for each operation.
# Show the user’s name and balance after actions.
# Handle invalid menu choices with an error message.
# Use float for balance.


import random


def bank_name():
    names = ["NBE", "Banque Misr", "Banque du Caire", "CIB",
             "AlexBank", "QNB", "AAIB", "HDB", "SCB", "NBK", "ABC"]
    return random.choice(names)


def creating_account():
    name = input("Enter Your Name: ")
    balance = float(input("Enter Your Initial balance: \n"))
    return name, balance


def check_balance(name, balance):
    print(f"{name}: Your balance is {balance:.2f}\n")


def deposit(balance):
    amount = float(input("Enter amount to deposit: \n"))
    if amount > 0:
        balance += amount
        print(f"Deposited: {amount}")
        print(f"Your Current Balance is {balance}")
        return balance, True
    else:
        print("Amount Must Be Positive, Please Try Again")
        return balance, False


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: \n"))
    if amount > 0:
        balance -= amount
        print(f"Withdrawn: {amount}")
        print(f"Your Current Balance is {balance}")
        return balance, True
    else:
        print("Amount Must Be Positive, Please Try Again")
        return balance, False


def main():
    print(f"Welcome to {bank_name()}")
    name, balance = creating_account()

    while True:
        print("********** Main Menu **********\n")
        print("1 -> Check balance")
        print("2 -> deposit")
        print("3 -> withdraw")
        print("4 -> Exit\n")
        choice = input("Enter Your Choice: \n")

        if choice == "1":
            check_balance(name, balance)
            print("Thank You For Visiting Us!")
            break

        elif choice == "2":
            balance, success = deposit(balance)
            if success:
                print("Thank You For Visiting Us!")
                break

        elif choice == "3":
            balance, success = withdraw(balance)
            if success:
                print("Thank You For Visiting Us!")
                break

        elif choice == "4":
            print("Thank You For Visiting Us!")
            break

        else:
            print("Invalid Choice, Please Try Again")


main()
