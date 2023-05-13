from typing import List


def findMaxK(nums: List[int]) -> int:
    maxNum = -1
    dicts = set()
    for num in nums:
        if -num in dicts:
            maxNum = max(abs(num), maxNum)
        else:
            dicts.add(num)
    return maxNum
