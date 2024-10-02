
class Account:

    def __init__(self, balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    

    def withDrawAmount(self, balance):
        self.balance -= balance


    def depositAmount(self, balance):
        self.balance += balance    
