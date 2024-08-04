def subtractProductAndSum(n: int) -> int:
    n = map(int, list(str(n)))
    temp = 1
    temp1 = 0
    for item in n:
        temp *= item
        temp1 += item
    return temp-temp1