# bank_account.py: Defines the BankAccount class for OOP demonstration.

class BankAccount:
    """
    Represents a simple bank account with basic deposit, withdrawal, and balance display features.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes the account with an optional initial balance.
        :param initial_balance: The starting balance for the account.
        """
        # Encapsulation: Storing the balance in a private-like attribute (conventionally)
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        :param amount: The positive amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
            
    def withdraw(self, amount):
        """
        Withdraws the specified amount if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
