from typing import List
from math import floor, sqrt


def repairCars(ranks: List[int], cars: int) -> int:
    left, right = 1, max(ranks) * cars * cars

    def check(middle):
        return sum([floor(sqrt(middle // x)) for x in ranks]) >= cars

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
