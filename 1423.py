from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    ans = sum(cardPoints[:k])
    index = k - 1
    temp = ans
    while index >= 0:
        temp = temp - cardPoints[index] + cardPoints[-(k-index)]
        ans = max(ans, temp)
        index = index - 1
    return ans