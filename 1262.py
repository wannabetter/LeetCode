from typing import List


def maxSumDivThree(nums: List[int]) -> int:
    ans = 0
    a = [num for num in nums if num % 3 == 0]
    b = sorted([num for num in nums if num % 3 == 1], reverse=True)
    c = sorted([num for num in nums if num % 3 == 2], reverse=True)

    lb, lc = len(b), len(c)
    for cntb in [lb - 2, lb - 1, lb]:
        if cntb >= 0:
            for cntc in [lc - 2, lc - 1, lc]:
                if cntc >= 0 and (cntb - cntc) % 3 == 0:
                    ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
    return ans + sum(a)
