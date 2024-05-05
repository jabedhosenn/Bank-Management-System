class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def show_users(self):
        self.bank.show_users()

    def total_balance(self):
        self.bank.total_balance()

    def total_loan(self):
        self.bank.total_loan()

    def off_loan(self):
        self.bank.off_loan()

    def on_loan(self):
        self.bank.on_loan()

    def bank_balance(self):
        return self.bank.bank_balance()

    def bank_loan(self):
        return self.bank.bank_loan()