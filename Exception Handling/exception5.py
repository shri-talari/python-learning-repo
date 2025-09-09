'''Q5. ATM Simulator

Problem:
Simulate a simple ATM system.

The account starts with balance = 1000.

User can:

Deposit money

Withdraw money

Check balance

Exit

Handle exceptions:

Non-integer deposit/withdraw amount (ValueError).

Withdrawal amount greater than balance (Exception).'''


def atm_simulator():
    balance = 1000

    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == "1":
                amount = int(input("Enter amount to deposit: "))
                if amount <= 0:
                    raise ValueError("Deposit amount must be positive!")
                balance += amount
                print(f"Deposited {amount}. New balance: {balance}")

            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive!")
                if amount > balance:
                    raise Exception("Insufficient balance!")
                balance -= amount
                print(f"Withdrew {amount}. New balance: {balance}")

            elif choice == "3":
                print(f"Current balance: {balance}")

            elif choice == "4":
                print("Exiting... Thank you for using the ATM.")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


atm_simulator()
