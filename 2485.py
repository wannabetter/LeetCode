def pivotInteger(n: int) -> int:
    if n == 1:
        return 1
    for index in range(n - 1, -1, -1):
        if ((1 + index) / 2 * index) == ((index + n) / 2 * (n - index + 1)):
            return index
    return -1