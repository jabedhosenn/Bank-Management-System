from admin import Admin
from bank import Bank

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
                        print(f"Amount {amount} is successfully deposited.")
                        break
                else:
                    print("Account not found.")

            elif user_choice == 3:
                account_number = int(input("Enter your account number: "))
                amount = int(input("Enter the amount you want to withdraw: "))
                for user in bank.accounts:
                    if user.account_number == account_number:
                        if user.balance >= amount:
                            user.withdraw(amount)
                            print(f"Amount {amount} is withdraw successfully.")
                        else:
                            print("Withdrawal amount exceeded!")
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
                        print(f"Loan amount {amount} is taken successfully.")
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
                    print(f"Amount {amount} is successfully Transfared.")
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
            print("8. Total bank loan")
            print("9. Exit")

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
                admin.bank_loan()

            elif admin_choice == 9:
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