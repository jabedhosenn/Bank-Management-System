from users import User

class Bank:
    def __init__(self):
        self.accounts = []
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.accounts.append(user)
        print(f"Account created successfully. Account Number: {user.account_number}")
        return user

    def delete_account(self, account_number):
        for user in self.accounts:
            if user.account_number == account_number:
                self.accounts.remove(user)
                print(f"Account with account number {account_number} deleted successfully.")
                return
        print("Account not found.")

    def show_users(self):
        print("List of Users:")
        for user in self.accounts:
            print(f"Accounr Number: {user.account_number}, Name: {user.name}, Email: {user.email}, Account Type: {user.account_type}")

    def total_balance(self):
        total_balance = sum(user.balance for user in self.accounts)
        print(f"Total Balance: {total_balance}")

    def total_loan(self):
        total_loan = sum(user.loan_taken for user in self.accounts)
        print(f"Total Loan: {total_loan}")

    def off_loan(self):
        self.loan_feature_enabled = False
        print("Loan feature is now disabled.")

    def on_loan(self):
        self.loan_feature_enabled = True
        print("Loan feature is now enabled.")

    def bank_balance(self):
        bank_balance = sum(user.balance for user in self.accounts)
        print(f"Total Bank Balance: {bank_balance}")

    def bank_loan(self):
        bank_loan = sum(user.loan_taken for user in self.accounts)
        print(f"Total Bank Loan: {bank_loan}")