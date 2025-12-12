class Bank_account:
    def __init__(self, owner,balance):
        self.owner= owner
        self.balance = balance
        
    def deposit (self,amount):
        self.balance +=amount 
        print(f"deposited: {amount}.New balance: {self.balance} ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insuffiecient funds!") 
        else:
            self.balance==amount
            print(f"withdrew: {amount}.new balance: {self.balance}")
    def check_balance(self):
         return f"current balance: {self.balance}"

account= Bank_account("Muneza", 4000)

account.deposit(4000)
account.withdraw(1000)
print(account.check_balance())
