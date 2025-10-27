"""
Create a  BankAccount  class with:
 Attributes:  account_holder ,  balance  (initial value 0)
 Method:  deposit(amount)  - balance increase kare
 Method:  withdraw(amount)  - balance decrease kare
 Method:  show_balance()  - current balance display kare
 Expected Output:
 Balance: ₹1000
 Withdrawn: ₹200
 Balance: ₹800
"""


class Bank_account:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self,deposit_balance):
        self.balance += deposit_balance
        print(f"Balance: {self.balance}")

    def withdraw(self,withdraw_amt):
            if withdraw_amt <= self.balance:
                 self.balance -= withdraw_amt
                 print(f"Withdrawn: {withdraw_amt}")
            else:
                 print("Not Enough amount to withdraw")
                 

    def show_balance(self):
        balance = self.balance
        print(f"Balance: {self.balance}")

my_account = Bank_account("Arun Yadav")
my_account.deposit(1000)
my_account.withdraw(800)
my_account.show_balance()
