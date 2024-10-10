from datetime import datetime

class BankAccount:
    def __init__(self, account_number, name, date_of_birth, date_of_opening, balance=0):
        self.account_number = account_number
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.transactions = []

    def view_account_details(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.name}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Date of Account Opening: {self.date_of_opening}\n"
            f"Balance: {self.balance}"
        )

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"Amount {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def print_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, date_of_birth, initial_balance=0):
        date_of_opening = datetime.now().strftime("%Y-%m-%d")
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(
                account_number, name, date_of_birth, date_of_opening, initial_balance
            )
            print(f"Account created successfully for {name} with Account Number: {account_number}")
        else:
            print("Account number already exists.")

    def view_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account.view_account_details())
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def fund_transfer(self, from_account, to_account, amount):
        from_acc = self.accounts.get(from_account)
        to_acc = self.accounts.get(to_account)
        if from_acc and to_acc:
            if from_acc.balance >= amount:
                from_acc.withdraw(amount)
                to_acc.deposit(amount)
                print(f"Successfully transferred {amount} from Account {from_account} to Account {to_account}")
            else:
                print("Insufficient funds in the source account.")
        else:
            print("One or both accounts not found.")

    def print_transactions(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_transactions()
        else:
            print("Account not found.")


def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Bank Application")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Fund Transfer")
        print("6. Print Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter Account Number: ")
            name = input("Enter Account Holder's Name: ")
            date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
            initial_balance = float(input("Enter Initial Balance: "))
            bank.create_account(account_number, name, date_of_birth, initial_balance)

        elif choice == '2':
            account_number = input("Enter Account Number: ")
            bank.view_account_details(account_number)

        elif choice == '3':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Deposit: "))
            bank.deposit(account_number, amount)

        elif choice == '5':
            from_account = input("Enter From Account Number: ")
            to_account = input("Enter To Account Number: ")
            amount = float(input("Enter Amount to Transfer: "))
            bank.fund_transfer(from_account, to_account, amount)

        elif choice == '6':
            account_number = input("Enter Account Number: ")
            bank.print_transactions(account_number)

        elif choice == '7':
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
