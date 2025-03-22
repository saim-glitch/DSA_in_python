class Bankaccout():
    def __init__(self,name,phone,country,balance):
        self.name=name
        self.phone_no=phone
        self.country_name=country
        self.balance=balance

    def balance(self):
        print(f"{self.name}, You have a balance of {self.balance}")
    
    def deposit_funds(self,amount):
        self.balance+=amount
        print(f"{self.name},you have successfully deposited the funds.Now your current balance is {self.balance} ")

    def withdraw_funds(self,amount):
        self.amount=amount
        if self.balance < amount:
            print(f"{self.name},You have insufficient balance,Plz deposit funds or try with other amount,current balance is {self.balance}")
        else:
            self.balance-=amount
            print(f"{self.name},You have successfully withdrawed a balance of{self.amount} ,your current balce is {self.balance}")


person1=Bankaccout("saim",93096527207,"Pakistan",10000)
print(person1.balance)
print(person1.deposit_funds(10000))
print(person1.withdraw_funds(567))
