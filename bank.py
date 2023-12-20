
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            return f"Account {account_number} created with an initial balance of ${initial_balance}"
        else:
            return f"Account {account_number} already exists."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            return f"Deposited ${amount} into account {account_number}. New balance: ${self.accounts[account_number]}"
        else:
            return f"Account {account_number} does not exist."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                return f"Withdrew rs{amount} from account {account_number}. New balance: ${self.accounts[account_number]}"
            else:
                return f"Insufficient funds in account {account_number}."
        else:
            return f"Account {account_number} does not exist."

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return f"Account {account_number} balance: rs{self.accounts[account_number]}"
        else:
            return f"Account {account_number} does not exist."
