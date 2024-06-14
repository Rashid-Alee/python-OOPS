# Importing the abstract base class module
from abc import ABC, abstractmethod


# Abstract Class for Bank Accounts
class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Common attribute for all accounts
        self.balance = balance  # Common attribute for all accounts

    @abstractmethod
    def deposit(self, amount):
        pass  # Abstract method to be implemented by subclasses

    @abstractmethod
    def withdraw(self, amount):
        pass  # Abstract method to be implemented by subclasses

    def display_details(self):
        # Common method to display account details
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


# Concrete Class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Specific attribute for savings account

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def display_details(self):
        super().display_details()
        print(f"Interest Rate: {self.interest_rate}%")


# Concrete Class for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = (
            transaction_limit  # Specific attribute for checking account
        )

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.transaction_limit:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
        else:
            print("Transaction exceeds limit or insufficient balance.")

    def display_details(self):
        super().display_details()
        print(f"Transaction Limit: ${self.transaction_limit:.2f}")


# Concrete Class for Business Account
class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = (
            overdraft_limit  # Specific attribute for business account
        )

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
        else:
            print("Exceeds overdraft limit.")

    def display_details(self):
        super().display_details()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")


# Creating objects of SavingsAccount, CheckingAccount, and BusinessAccount
savings = SavingsAccount("SA123", 1000.0, 3.5)
checking = CheckingAccount("CA456", 500.0, 200.0)
business = BusinessAccount("BA789", 2000.0, 1000.0)

# Displaying details and performing operations
print("Savings Account Details:")
savings.display_details()
savings.deposit(500)
savings.withdraw(300)

print("\nChecking Account Details:")
checking.display_details()
checking.deposit(300)
checking.withdraw(600)

print("\nBusiness Account Details:")
business.display_details()
business.deposit(1000)
business.withdraw(2500)
