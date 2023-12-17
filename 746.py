from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    prev = curr = 0
    for index in range(2, n + 1):
        nxt = min(curr + cost[index - 1], prev + cost[index - 2])
        prev, curr = curr, nxt
    return curr