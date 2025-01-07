class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Current balance is {self.balance}.")

# Example usage
account = BankAccount("123456789", "pem tshering sherpa", 1000)
account.deposit(120000)
account.withdraw(2200)
account.display_balance()