class Bankaccount:
    def __init__(self, name, bankbalance, raast_id, account_no):
        self.name = name
        self.bankbalance = bankbalance
        self.raast_id = raast_id
        self.account_no = account_no

    def deposit(self, amount):
        self.bankbalance += amount
        print(f"You have successfully deposited {amount}. Total balance: {self.bankbalance}")

    def withdraw(self, amount):
        if self.bankbalance < amount:
            print("Insufficient funds. Please deposit more funds.")
        else:
            self.bankbalance -= amount
            print(f"You withdrew {amount}. Remaining balance: {self.bankbalance}")

# Object creation (Outside the class)
person1 = Bankaccount("Saim", 10000, 1234, 9876)

# Withdraw an amount greater than the balance
person1.withdraw(20000)
