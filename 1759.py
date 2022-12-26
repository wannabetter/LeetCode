from itertools import groupby


def countHomogenous(s: str) -> int:
    Res = 0
    for Key, Group in groupby(s):
        n = len(list(Group))
        Res += (n + 1) * n // 2
    return Res % (10 ** 9 + 7)
