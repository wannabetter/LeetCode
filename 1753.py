def maximumScore(a: int, b: int, c: int) -> int:
    Arr = sorted([a, b, c])
    if Arr[0] + Arr[1] <= Arr[2]:
        return Arr[0] + Arr[1]
    return sum(Arr) // 2
