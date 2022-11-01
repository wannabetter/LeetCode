from typing import List


def averageValue(nums: List[int]) -> int:
    Avg = 0
    Item = 0
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            Avg += num
            Item += 1
    return Avg // Item if Item else 0
