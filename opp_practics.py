class Bankaccount:
    def __init__(self,name,bankbalance,raast_id,account_no):
        self.name=name
        self.bankbalance=bankbalance
        self.raast_id=raast_id
        self.account_no=account_no

    def deposit(self,amount):
        self.bankbalance +=amount
        print(f"You have successfully deposit the funds of {amount}, total amount is {self.bankbalance}")

    def withdraw(self,amount):
        if self.bankbalance < amount:
            print(f"Your bankaccount have less amount. Plz deposit funds")
        else:
            self.bankbalance -=amount
            print(f"You withdrew the amount {amount} .Your total amount is {self.bankbalance}")


person1=Bankaccount("saim",10000,1234,9876)
person=person1.withdraw(20000)
print(person)
