from typing import List


def getMaximumConsecutive(coins: List[int]) -> int:
    coins.sort()
    ans = 0
    for coin in coins:
        if coin > ans+1:
            return ans+1
        ans += coin
    return ans+1
