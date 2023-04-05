def commonFactors(a: int, b: int) -> int:
    res = 1
    for num in range(2, min(a, b) + 1):
        if a % num == 0 and b % num == 0:
            res += 1
    return res
