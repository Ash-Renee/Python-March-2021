class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.int_rate = int_rate
        self.account_balance = balance
        self.yield_int = self.account_balance * self.int_rate
        self.name = name

    def yield_interest(self):
        self.yield_int-+ = self.account_balance * self.int_rate

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


Checking = BankAccount("Checking", .05, 100)
Savings = BankAccount("Savings", .07, 125)

Checking.display_account_info()
Savings.display_account_info()


Checking.make_deposit(123).make_deposit(55).make_deposit(77).make_withdrawal(111).display_account_info()
Savings.make_deposit(73).make_deposit(872).make_withdrawal(500).make_withdrawal(123).make_withdrawal(75).make_withdrawal(375).display_account_info()