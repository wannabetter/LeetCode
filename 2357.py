from typing import List


def minimumOperations(nums: List[int]) -> int:
    numSet = set(nums)
    return len(numSet) if 0 in numSet else len(numSet) - 1
