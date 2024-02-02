from typing import List


def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    values = [[a + b, a, b] for a, b in zip(aliceValues, bobValues)]
    values.sort(reverse=True)
    alice, bob = sum(value[1] for value in values[::2]), sum(value[2] for value in values[1::2])

    return 0 if bob == alice else 1 if alice > bob else -1
