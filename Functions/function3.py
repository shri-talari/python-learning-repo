'''Q3. Bank Account Simulation

Problem:
Write a program with functions to simulate a simple bank system:

deposit(balance, amount) → adds money and returns new balance

withdraw(balance, amount) → subtracts money if balance is enough, else prints "Insufficient funds".

account_summary(transactions) → takes a list of transactions (as dictionaries) and returns total deposits, total withdrawals, and final balance.'''


def deposit(balance, amount, transactions):
    if amount <= 0:
        print("Invalid deposit amount.")
        return balance
    balance += amount
    transactions.append({"Deposit": amount})
    return balance


def withdraw(balance, amount, transactions):
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return balance
    if balance >= amount:
        balance -= amount
        transactions.append({"Withdraw": amount})
    else:
        print("Insufficient Balance for the Transaction")
    return balance


def account_summary(transactions, balance):
    deposits = [x for x in transactions if "Deposit" in x]
    withdrawals = [x for x in transactions if "Withdraw" in x]
    total_deposit = sum(x["Deposit"] for x in deposits)
    total_withdraw = sum(x["Withdraw"] for x in withdrawals)
    print(
        f"Final Balance: {balance}\n Total Deposited: {total_deposit}\n Total Withdrawn: {total_withdraw}")


balance = 1000
transactions = []
input_count = int(input("Enter the count of transactions to perform : "))
print("Enter deposit or withdraw for each transaction what to perform : ")
for i in range(input_count):
    choice = input(f"Transaction {i+1} (deposit/withdraw) : ").strip().lower()
    amount = int(input("Amount : "))
    if choice == "deposit":
        balance = deposit(balance, amount, transactions)
    elif choice == "withdraw":
        balance = withdraw(balance, amount, transactions)
    else:
        print("Please only enter a valid operation deposit or withdraw")
account_summary(transactions, balance)
