def waysToBuyPensPencils(total: int, cost1: int, cost2: int) -> int:
    ans = 0
    cost1, cost2 = max(cost1, cost2), min(cost1, cost2)
    for index in range(total // cost1 + 1):
        cur = total - cost1 * index
        ans = ans + cur//cost2 + 1
    return ans