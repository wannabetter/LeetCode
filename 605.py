from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    seen = set([id if flower else -2 for id, flower in enumerate(flowerbed)])
    for id, flower in enumerate(flowerbed):
        if flower == 0 and (id + 1 not in seen and id - 1 not in seen):
            seen.add(id)
            n = n - 1
    return n <= 0