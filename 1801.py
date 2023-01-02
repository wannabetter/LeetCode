from typing import List
from bisect import insort


def getNumberOfBacklogOrders(orders: List[List[int]]) -> int:
    Order, Sell = [], []
    for price, amount, ordertype in orders:
        if ordertype == 0:
            while amount and Sell and Sell[0][0] <= price:
                if Sell[0][1] > amount:
                    Sell[0][1] -= amount
                    amount = 0
                elif Sell[0][1] == amount:
                    Sell.pop(0)
                    amount = 0
                else:
                    amount -= Sell[0][1]
                    Sell.pop(0)
            if amount > 0:
                insort(Order, [price, amount])
        else:
            while amount and Order and price <= Order[-1][0]:
                if Order[-1][1] > amount:
                    Order[-1][1] -= amount
                    amount = 0
                elif Order[-1][1] == amount:
                    Order.pop()
                    amount = 0
                else:
                    amount -= Order[-1][1]
                    Order.pop()
            if amount > 0:
                insort(Sell, [price, amount])
    return (sum(amount for _, amount in Sell) + sum(amount for _, amount in Order)) % (10 ** 9 + 7)
