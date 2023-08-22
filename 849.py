from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    ans, left = 0, 0
    while left < len(seats) and seats[left] == 0:
        left = left + 1
    ans = max(ans, left)
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right = right + 1
        if right == len(seats):
            ans = max(ans, right - left - 1)
        else:
            ans = max(ans, (right - left) // 2)
        left = right
    return ans
