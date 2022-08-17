from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.Money = balance
        self.person = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.person or account2 > self.person:
            return False
        if self.Money[account1 - 1] >= money:
            self.Money[account1 - 1] = self.Money[account1 - 1] - money
            self.Money[account2 - 1] = self.Money[account2 - 1] + money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account > self.person:
            return False
        self.Money[account - 1] = self.Money[account - 1] + money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.person:
            return False
        if self.Money[account - 1] >= money:
            self.Money[account - 1] = self.Money[account - 1] - money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
