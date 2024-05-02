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
        return sum(user.balance for user in self.accounts)

    def bank_loan(self):
        return sum(user.loan_taken for user in self.accounts)

# Admin class
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


bank = Bank()
admin = Admin(bank)

while True:
    print("\nWelcome to the Central Bank of Noakhali")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice(1-3): "))

    if choice == 1:
        while True:
            print("\nUser:")
            print("1. Create an account")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Show balance")
            print("5. Check transaction history")
            print("6. Take a loan")
            print("7. Transfer money")
            print("8. Exit")

            user_choice = int(input("Enter your choice(1-8): "))

            if user_choice == 1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                account_type = input("Enter your account type: ")

                admin.create_account(name, email, address, account_type)

            elif user_choice == 2:
                account_number = int(input("Enter your account number: "))
                amount = int(input("Enter the amount you want to deposit: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        user.deposit(amount)
                        print("Deposit successful.")
                        break
                else:
                    print("Account not found.")

            elif user_choice == 3:
                account_number = int(input("Enter your account number: "))
                amount = int(input("Enter the amount you want to withdraw: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        user.withdraw(amount)
                        print("Withdrawal successful.")
                        break
                else:
                    print("Account not found.")

            elif user_choice == 4:
                account_number = int(input("Enter your account number: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        print(f"Balance: {user.check_balance()}")
                        break
                else:
                    print("Account not found.")

            elif user_choice == 5:
                account_number = int(input("Enter your account number: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        print("Transaction History:")
                        for transaction in user.check_transaction_history():
                            print(transaction)
                        break
                else:
                    print("Account not found.")

            elif user_choice == 6:
                account_number = int(input("Enter your account number: "))
                amount = int(input("Enter the amount you want to take loan: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        user.take_loan(amount)
                        print("Loan taken successfully.")
                        break
                else:
                    print("Account not found.")

            elif user_choice == 7:
                sender_account_number = int(input("Enter your account number: "))
                recipient_account_number = int(input("Enter the recipient's account number: "))
                amount = int(input("Enter the amount you want to transfer: "))
                sender = None
                recipient = None
                for user in bank.accounts:
                    if user.account_number == sender_account_number:
                        sender = user
                    elif user.account_number == recipient_account_number:
                        recipient = user
                if sender and recipient:
                    sender.transfer(amount, recipient)
                    print("Transfer successful.")
                else:
                    print("Invalid account numbers.")

            elif user_choice == 8:
                print("Returning to main menu...")
                break

            else:
                print("Invalid choice. Please choose again.")

    elif choice == 2:
        while True:
            print("\nAdmin:")
            print("1. Create an account")
            print("2. Delete an account")
            print("3. Show users")
            print("4. Total balance")
            print("5. Total loan")
            print("6. Turn off loan feature")
            print("7. Turn on loan feature")
            print("8. Exit")

            admin_choice = int(input("Enter your choice(1-8): "))

            if admin_choice == 1:
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter user's account type: ")
                admin.create_account(name, email, address, account_type)

            elif admin_choice == 2:
                account_number = int(input("Enter the account number you want to delete: "))
                admin.delete_account(account_number)

            elif admin_choice == 3:
                admin.show_users()

            elif admin_choice == 4:
                admin.total_balance()

            elif admin_choice == 5:
                admin.total_loan()

            elif admin_choice == 6:
                admin.off_loan()

            elif admin_choice == 7:
                admin.on_loan()

            elif admin_choice == 8:
                print("Returning to main menu...")
                break

            else:
                print("Invalid choice. Please choose again.")
    
    elif choice == 3:
        print("Exiting...")
        breaking = input("Press any key to continue...")
        break

    else:
        print("Invalid choice. Please choose again.")