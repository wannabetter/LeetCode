def climbStairs(n: int) -> int:
    p, q, r = 0, 0, 1
    for i in range(1, n + 1):
        p = q
        q = r
        r = p + q
    return r
