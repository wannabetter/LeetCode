from collections import defaultdict


def countPoints(rings: str) -> int:
    Cnt = defaultdict(set)
    for index in range(0, len(rings), 2):
        Cnt[rings[index + 1]].add(rings[index])

    ans = 0
    for index in range(0, 10):
        if len(Cnt[str(index)]) == 3:
            ans += 1
    return ans
