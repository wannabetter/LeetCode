from typing import List
from collections import Counter


def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    if upper + lower != sum(colsum):
        return []
    if Counter(colsum)[2] > min(upper, lower):
        return []

    ans = [[], []]
    for col in colsum:
        if col == 2:
            ans[0].append(1)
            ans[1].append(1)
            upper = upper - 1
            lower = lower - 1
        elif col == 1:
            if upper > lower:
                ans[0].append(1)
                ans[1].append(0)
                upper = upper - 1
            else:
                ans[0].append(0)
                ans[1].append(1)
                lower = lower - 1
        else:
            ans[0].append(0)
            ans[1].append(0)
    return ans
