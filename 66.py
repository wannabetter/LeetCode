from typing import List


def plusOne(digits: List[int]) -> List[int]:
    Res = []
    Sum = 0
    for digit in digits:
        Sum = Sum * 10 + digit
    Sum = Sum + 1
    while Sum != 0:
        Temp = Sum % 10
        Res.insert(0, Temp)
        Sum = Sum // 10
    return Res