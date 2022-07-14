from typing import List


def singleNumber(nums: List[int]) -> int:
    Res = 0
    for num in nums:
        Res = Res ^ num
    return Res
