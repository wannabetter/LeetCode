def checkPowersOfThree(n: int) -> bool:
    while n:
        if n % 3 == 2:
            return False
        n = n // 3
    return True
