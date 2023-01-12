from functools import lru_cache


@lru_cache(None)
def minDays(n: int) -> int:
    if n <= 1:
        return n
    return 1 + min(n % 2 + minDays(n // 2), n % 3 + minDays(n // 3))
