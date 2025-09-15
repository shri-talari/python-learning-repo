'''Q1. Bank Account System (Encapsulation + Exception Handling)**

Problem:

Create a BankAccount class with:

Attributes: account_number, holder_name, balance (private).

Methods:

deposit(amount) → adds money (handle invalid inputs).

withdraw(amount) → subtracts money (raise exception if insufficient funds).

get_balance() → returns balance.

Create multiple accounts and allow transactions.

Store transaction history in a file.'''


class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.holder_name}\nBalance: {self.__balance}"

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.__balance += amount
            try:
                with open("transactions.txt", "a") as f:
                    f.write(
                        f"Deposited {amount}Rs into, Account {self.account_number} and Balance {self.__balance}\n")
            except FileNotFoundError:
                print("Deposit Transaction Failed! Please try again")
        else:
            print("Amount to be deposited must be only numbers!")

    def withdraw(self, amount):
        if self.__balance >= amount:
            try:
                with open("transactions.txt", "a") as f:
                    f.write(
                        f"{amount}Rs Withdrawn successfully from Account {self.account_number}\n")
            except Exception:
                print("Withdrawal Request Failed! Please try again")
            else:
                self.__balance -= amount
        else:
            try:
                raise ValueError("Insufficient Balance! Withdrawal Failed.")
            except ValueError as e:
                with open("transactions.txt", "a") as f:
                    f.write(f"{e}\n")
                    print(e)

    def get_balance(self):
        try:
            with open("transactions.txt", "a") as f:
                f.write(
                    f"Final Balance for Account {self.account_number} : {self.__balance}\n")
                print(
                    f"Current Balance for Account {self.account_number}: {self.__balance}")
        except Exception:
            print("Unable to fetch balance! Please try again")


person1 = BankAccount(101, "Alice", 10000)
person2 = BankAccount(102, "Bob", 5000)
person3 = BankAccount(103, "Charlie", 8000)

person2.deposit(3000)
person2.get_balance()

person3.withdraw(12000)
person3.deposit(2000)
person3.get_balance()

person1.withdraw(5000)
person1.get_balance()
