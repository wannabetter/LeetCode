from typing import List


def minimumRemoval(beans: List[int]) -> int:
    n = len(beans)
    beans = sorted(beans)

    total = sum(beans)
    ans = total

    for index in range(n):
        ans = min(ans, total - beans[index] * (n - index))
    return ans
