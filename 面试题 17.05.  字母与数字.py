from typing import List
from itertools import accumulate


def findLongestSubarray(array: List[str]) -> List[str]:
    arr = list(accumulate((-1 if v.isdigit() else 1 for v in array), initial=0))
    first = {}
    begin = end = 0
    for index, val in enumerate(arr):
        j = first.get(val, -1)
        if j < 0:
            first[val] = index
        elif index - j > end - begin:
            begin, end = j, index
    return array[begin:end]