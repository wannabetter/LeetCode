def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1))
