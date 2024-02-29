class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount :.2f} has been deposited in your account.")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            return self.balance

    def check_balance(self, current_balance):
        print(f"Current balance is ${current_balance :.2f}.")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self, interest_rate, time):
        interest = (self.balance * interest_rate * time) / 100
        total_amount = self.balance + interest
        print(f'Amount with interest per {time} year = {total_amount :.2f}')
        return total_amount


number_of_account = input('Insert bank account number: ')
curr_balance = 0
bank_account = BankAccount(number_of_account, curr_balance)
operation = input(
        """Select operation:
        1. Deposit
        2. Withdraw
        3. Show current balance
        4. Make a saving account
        5. Quit
        """)
while True:
    if operation == 'YES':
        operation = input(
            """Select operation:
            1. Deposit
            2. Withdraw
            3. Show current balance
            4. Make a saving account
            5. Quit
            """)

    if operation == '1':
        current_amount = float(input('Insert deposit amount: '))
        curr_balance = bank_account.deposit(current_amount)
    elif operation == '2':
        current_amount = float(input('Insert withdraw amount: '))
        curr_balance = bank_account.withdraw(current_amount)
    elif operation == '3':
        bank_account.check_balance(curr_balance)
    elif operation == '4':
        period = int(input('Add period in year: '))
        interest_percent = float(input('Add percent per interest: '))
        saving_account = SavingsAccount(number_of_account, curr_balance)
        curr_balance = saving_account.calculate_interest(interest_percent, period)
    elif operation == '5' or operation == 'NO':
        print('Have a nice day!')
        bank_account.adding_info()
        break
    else:
        print('Invalid Input. Try Again')
        operation = input("""Select operation:
                              1. Deposit
                              2. Withdraw
                              3. Show current balance
                              4. Make a saving account
                              5. Quit
                              """)
    operation = input("Do you want to continue: YES/NO: ")
