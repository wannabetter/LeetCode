from typing import List


def giveGem(gem: List[int], operations: List[List[int]]) -> int:
    for send, recv in operations:
        temp = gem[send] // 2
        gem[send] = gem[send] - temp
        gem[recv] = gem[recv] + temp
    return max(gem) - min(gem)