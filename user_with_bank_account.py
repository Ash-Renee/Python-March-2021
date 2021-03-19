class BankAccount:   #from the previous assignment
    def __init__(self, name, int_rate, balance):
        self.yield_int = int_rate
        self.account_balance = balance
        self.name = name

    def yield_interest(self):
        self.yield_int += self.account_balance * self.int_rate

    def deposit(self, amount):
        self.account_balance += amount
        self.yield_interest()
        return self

    def withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("You just made a YUGE mistake")
        self.yield_interest()
        return self

    def display_account_info(self):
        print (f"self.name, self.int_rate, self.account_balance, self.yield_int")


class User:
    def __init__(self, name, email, account_name):
        self.name = name
        self.email = email
        self.account = account_name


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        if self.account.account_balance < 0:
            print("You done messed up A-A-Ron!")
        return self

    def transfer(self,other_user,amount):
        self.balance = amount
        other_user.account += amount
        return self

    # def account_balance(self):
    #     print(f"Balance: ${self.account_balance}, int_rate: {int_rate}")
    #     return self

Checking_1 = BankAccount("Checking_1", .05, 100)
Checking_2 = BankAccount("Checking_2", .07, 150)
Savings = BankAccount("Savings", .09, 200)

Ashley = User("Ashley D'Allessandro", "ashley.dallessandro@gmail.com", Savings)
Sarah = User("Sarah Tonin", "sarah@tonin.com", Checking_1)
Paige = User("Paige Pupper", "paige@pupper.com", Checking_1)

Ashley.make_deposit(125).account_balance()