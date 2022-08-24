from typing import List
from collections import Counter


def canBeEqual(target: List[int], arr: List[int]) -> bool:
    cnt, ans = Counter(target), Counter(arr)
    return cnt == ans
