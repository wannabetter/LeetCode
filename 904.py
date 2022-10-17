from typing import List
from collections import Counter


def totalFruit(fruits: List[int]) -> int:
    Cnt = Counter()
    Left, Max = 0, 0
    for Right, fruit in enumerate(fruits):
        Cnt[fruit] += 1
        while len(Cnt) > 2:
            Cnt[fruits[Left]] -= 1
            if Cnt[fruits[Left]] == 0:
                Cnt.pop(fruits[Left])
            Left += 1
        Max = max(Max, Right - Left + 1)
    return Max
