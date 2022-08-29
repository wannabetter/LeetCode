from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    Res = []
    for index in range(n):
        Res.append(nums[index])
        Res.append(nums[index + n])
    return Res
