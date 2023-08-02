from math import inf
from typing import List


def flipgame(fronts: List[int], backs: List[int]) -> int:
    same = set()
    for front, back in zip(fronts, backs):
        if front == back:
            same.add(front)
    ans = inf
    for front, back in zip(fronts, backs):
        if front < ans and front not in same:
            ans = front
        if back < ans and back not in same:
            ans = back
    return ans if ans != inf else 0
