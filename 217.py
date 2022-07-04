import copy
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    Temp = list(set(copy.deepcopy(nums)))
    if len(Temp) == len(nums):
        return True
    return False
