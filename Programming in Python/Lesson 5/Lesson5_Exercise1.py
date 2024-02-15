# Exercise: Creating a Class for a Bank Account:

# Design a Python class representing a bank account.
# Include attributes such as account number, account holder name, and balance.
# Add methods for deposit, withdrawal, and displaying the account details.
# Create instances of the class and test the methods.

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        """
        Initialize the BankAccount with account number, account holder name, and an optional initial balance.
        """
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient balance is available.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_account_details(self):
        """
        Display the account details including account number, account holder name, and balance.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: ${self.balance}")

# Creating instances of the BankAccount class
account1 = BankAccount(account_number=123456, account_holder_name="John Doe", balance=1000)
account2 = BankAccount(account_number=789012, account_holder_name="Jane Smith")

# Testing the methods
account1.display_account_details()

account1.deposit(500)
account1.withdraw(200)

account2.display_account_details()

account2.deposit(1000)
account2.withdraw(1500)

# In this code:

# The __init__ method initializes the bank account with the provided account number, account holder name, and an optional initial balance.
# The deposit method allows you to deposit money into the account, updating the balance accordingly.
# The withdraw method allows you to withdraw money from the account, provided there is sufficient balance.
# The display_account_details method displays the account details.
# Finally, instances of the BankAccount class are created (account1 and account2), and the methods are tested on these instances.

# Example Pseudocode for this solution:

# Class BankAccount:
#     // Constructor to initialize the account
#     Method __init__(account_number, account_holder_name, balance=0):
#         Set self.account_number to account_number
#         Set self.account_holder_name to account_holder_name
#         Set self.balance to balance

#     // Method to deposit money into the account
#     Method deposit(amount):
#         If amount > 0:
#             Increase self.balance by amount
#             Print "Deposited $amount. New balance: $self.balance"
#         Else:
#             Print "Invalid deposit amount. Please enter a positive value."

#     // Method to withdraw money from the account
#     Method withdraw(amount):
#         If amount > 0 and amount <= self.balance:
#             Decrease self.balance by amount
#             Print "Withdrew $amount. New balance: $self.balance"
#         Else:
#             Print "Invalid withdrawal amount or insufficient balance."

#     // Method to display account details
#     Method display_account_details():
#         Print "Account Number: self.account_number"
#         Print "Account Holder: self.account_holder_name"
#         Print "Balance: $self.balance"

