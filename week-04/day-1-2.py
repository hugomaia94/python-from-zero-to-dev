class BankAccount:
    def __init__(
        self,
        owner,
        balance=0,
    ):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Sucess! New balance: ${self.balance:.2f}\n")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Sucess! New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Owner - {self.owner}\nBalance - {self.balance:.2f}\n")
