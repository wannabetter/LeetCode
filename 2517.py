from math import inf
from typing import List


def maximumTastiness(price: List[int], k: int) -> int:
    price.sort()
    left, right = 0, price[-1] - price[0]

    def Check(arr, K, tastiness):
        prev = -inf
        cnt = 0
        for x in arr:
            if x - prev >= tastiness:
                cnt += 1
                prev = x
        return cnt >= K

    while left < right:
        mid = (left + right + 1) // 2
        if Check(price, k, mid):
            left = mid
        else:
            right = mid - 1
    return left
