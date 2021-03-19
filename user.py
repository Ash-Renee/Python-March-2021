class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self


    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


Ashley = User("Ashley D'Allessandro", "ashley.dallessandro@gmail.com")
Sarah = User("Sarah Tonin", "sarah.tonin@gmail.com")
Sonic = User("Sonic the Hedgehog", "sonic@thehedgehog.com")

Ashley.make_deposit(300).make_deposit(175).make_deposit(87).make_withdrawal(23).display_user_balance()
# Ashley.make_deposit(175)
# Ashley.make_deposit(87)
# Ashley.make_withdrawal(23)
# Ashley.display_user_balance()

Sarah.make_deposit(400).make_withdrawal(200).make_withdrawal(177).display_user_balance()
# Sarah.make_deposit(200)
# Sarah.make_withdrawal(150)
# Sarah.make_withdrawal(177)
# Sarah.display_user_balance()

Sonic.make_deposit(333).make_withdrawal(122).make_withdrawal(145).make_withdrawal(137).display_user_balance()
# Sonic.make_withdrawal(122)
# Sonic.make_withdrawal(145)
# Sonic.make_withdrawal(137)
# Sonic.display_user_balance()

# Ashley.transfer_money(Sonic, 23)
# Ashley.display_user_balance()
# Sonic.display_user_balance()
