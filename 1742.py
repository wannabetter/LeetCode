from collections import Counter


def countBalls(lowLimit: int, highLimit: int) -> int:
    Max = 0
    Cnt = Counter()
    for num in range(lowLimit, highLimit + 1):
        key = sum(list(map(int, str(num))))
        Cnt[key] += 1
        Max = max(Max, Cnt[key])
    return Max
