# Bank Account Menu Driven Program

balance = 0

def display_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("1. Display Current Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice. Try again.")