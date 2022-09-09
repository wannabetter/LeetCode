from typing import List


def findRepeatNumber(nums: List[int]) -> int:
    Temp = [False] * len(nums)
    for num in nums:
        if not Temp[num]:
            Temp[num] = True
        else:
            return num
