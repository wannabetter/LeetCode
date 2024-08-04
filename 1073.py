from typing import List


def addNegabinary(arr1: List[int], arr2: List[int]) -> List[int]:
    res = []
    i, j, carry = len(arr1) - 1, len(arr2) - 1, 0
    while i >= 0 or j >= 0 or carry:
        x = carry
        if i >= 0:
            x += arr1[i]
        if j >= 0:
            x += arr2[j]

        if x >= 2:
            res.append(x - 2)
            carry = -1
        elif x >= 0:
            res.append(x)
            carry = 0
        else:
            res.append(1)
            carry = 1
        i -= 1
        j -= 1

    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res[::-1]
