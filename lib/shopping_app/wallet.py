from ownable import Ownable
class Wallet(Ownable):

    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount
