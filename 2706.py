from typing import List


def buyChoco(prices: List[int], money: int) -> int:
    prices.sort()
    return money - sum(prices[:2]) if money - sum(prices[:2]) >= 0 else money
