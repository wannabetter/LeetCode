from typing import List


def minCount(coins: List[int]) -> int:
    ans = 0
    for coin in coins:
        ans = ans + coin // 2 + coin % 2
    return ans
