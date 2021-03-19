class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.int_rate = int_rate
        self.account_balance = balance
        self.yield_int = self.account_balance * self.int_rate
        self.name = name

    def yield_interest(self):
        self.yield_int += self.account_balance * self.int_rate

    def make_deposit(self, amount):
        self.account_balance += amount
        self.yield_interest()
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("You just made a YUGE mistake")
        self.yield_interest()
        return self

    def display_account_info(self):
        print (self.name, self.int_rate, self.account_balance, self.yield_int)

class User:
    def __init__(self, name, account_name):
        self.name = name
        self.account = account_name

    def make_deposit(self, amount):
        self.account.make_deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.make_withdrawal(amount)
        return self

    def account_balance(self):
        self.account.display_account_info()


Checking = BankAccount("Checking", .05, 100)
Savings = BankAccount("Savings", .07, 125)

Ashley = User ("Ashley D'Allessandro", Checking)

Checking.display_account_info()
Savings.display_account_info()

Ashley.make_deposit(125).make_withdrawal(33).account_balance()