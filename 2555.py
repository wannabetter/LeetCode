from typing import List


def maximizeWin(prizePositions: List[int], k: int) -> int:
    pre = [0] * (len(prizePositions) + 1)
    ans = left = 0
    for right, p in enumerate(prizePositions):
        while p - prizePositions[left] > k:
            left += 1
        ans = max(ans, right - left + 1 + pre[left])
        pre[right + 1] = max(pre[right], right - left + 1)
    return ans