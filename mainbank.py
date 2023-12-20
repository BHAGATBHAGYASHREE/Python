
from bank import Bank

def print_message(message):
    print(message)

def main():
    bank = Bank()

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            print_message(bank.create_account(account_number, initial_balance))

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print_message(bank.deposit(account_number, amount))

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print_message(bank.withdraw(account_number, amount))

        elif choice == '4':
            account_number = input("Enter account number: ")
            print_message(bank.check_balance(account_number))

        elif choice == '5':
            print_message("Exiting the banking application. Goodbye!")
            break

        else:
            print_message("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
