from typing import List


def maxProfit(prices: List[int]) -> int:
    minPrice = prices[0]
    result = 0
    for price in prices:
        minPrice = min(price, minPrice)
        result = max(price - minPrice, result)
    return result
