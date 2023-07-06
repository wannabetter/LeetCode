from typing import List


def maximumEvenSplit(finalSum: int) -> List[int]:
    if finalSum % 2 != 0:
        return []

    ans = []
    index = 2
    while index <= finalSum:
        ans.append(index)
        finalSum = finalSum - index
        index = index + 2
    ans[-1] = ans[-1] + finalSum
    return ans
