class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")

    # Method to get the current balance
    def get_balance(self):
        return self.__balance


# Creating a bank account object
account = BankAccount("John Doe", 1000)

# Accessing and modifying balance through methods
account.deposit(500)  # Output: Deposited $500. New balance: $1500
account.withdraw(200)  # Output: Withdrew $200. New balance: $1300

# Trying to access the private balance attribute directly (will cause an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

# Getting the current balance using the public method
print(f"Current balance: ${account.get_balance()}")  # Output: Current balance: $1300
