from typing import List


def numTimesAllBlue(flips: List[int]) -> int:
    ans = right = 0
    for index, x in enumerate(flips):
        right = max(right, x)
        if right == index + 1:
            ans += 1
    return ans
