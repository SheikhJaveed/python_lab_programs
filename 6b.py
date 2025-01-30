class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, new balance: {self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance: {self.balance}")
    
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
