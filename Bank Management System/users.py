import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(100000, 999999)
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: +{amount}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded!")
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -{amount}')

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_taken += amount
            self.loan_count += 1
            self.deposit(amount)
            self.transaction_history.append(f'Loan Taken: +{amount}')
        else:
            print("You have reached the maximum limit of loans.")

    def transfer(self, amount, recipient):
        if not isinstance(recipient, User):
            print("Invalid recipient.")
        elif self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer to {recipient.name}: -{amount}')
            recipient.transaction_history.append(f'Transfer from {self.name}: +{amount}')
        else:
            print("Insufficient amount.")