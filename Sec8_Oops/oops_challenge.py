class Account:
    def __init__(self, owner= 'a', balance = 1):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance = self.balance - amount
        else:
            print("Can't widthdraw beyond Zero")
            
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}" 
            
my_account = Account('Aditya', 500)

my_account.deposit(4500)
my_account.withdraw(700)
print(my_account)
