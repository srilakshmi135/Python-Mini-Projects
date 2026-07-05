balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print("Amount Deposited Successfully!")
                print("Current Balance: ₹", balance)
            else:
                print("Enter a valid amount.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Enter a valid amount.")
            elif amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Current Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        elif choice == 4:
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter valid numbers only.")