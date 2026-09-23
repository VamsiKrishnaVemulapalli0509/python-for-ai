class BankAccount:
    """Represents a simple bank account with deposit and withdrawal operations."""

    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Remove money from the account if sufficient funds exist."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Return the current account balance."""
        return self.balance


# --- Program Execution & Demonstration ---
if __name__ == "__main__":
    # Object 1
    account1 = BankAccount(owner="Vamsi", account_number="ACC123", balance=100.0)
    account1.deposit(50)
    account1.withdraw(30)
    print(f"Vamsi's balance: {account1.get_balance()}")

    # Object 2
    account2 = BankAccount(owner="Krishna", account_number="ACC456", balance=200.0)
    account2.withdraw(80)
    print(f"Krishna's balance: {account2.get_balance()}")
