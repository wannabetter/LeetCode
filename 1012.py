from functools import lru_cache


# 数位DP
def numDupDigitsAtMostN(n: int) -> int:
    s = str(n)

    @lru_cache(None)
    def find(index: int, mask: int, limit: bool, num: bool) -> int:
        if index == len(s):
            return int(num)
        res = 0
        if not num:
            res = find(index + 1, mask, False, False)
        low = 0 if num else 1
        up = int(s[index]) if limit else 9
        for d in range(low, up + 1):
            if (mask >> d & 1) == 0:
                res += find(index + 1, mask | (1 << d), limit and d == up, True)
        return res
    return n-find(0,0,True,False)
