from collections import Counter


def balancedString(s: str) -> int:
    Cnt = Counter(s)
    n = len(s)
    if all(item <= n // 4 for item in Cnt.values()):
        return 0
    res, i = n, 0
    for j, char in enumerate(s):
        Cnt[char] -= 1
        while i <= j and all(item <= n // 4 for item in Cnt.values()):
            res = min(res, j - i + 1)
            Cnt[s[i]] += 1
            i += 1
    return res
