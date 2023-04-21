def smallestEvenMultiple(n: int) -> int:
    temp = n
    while temp % 2 != 0 or temp % n != 0:
        temp += 1
    return temp
