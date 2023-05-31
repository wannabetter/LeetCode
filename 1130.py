from typing import List


def mctFromLeafValues(arr: List[int]) -> int:
    res = 0
    stack = []
    for x in arr:
        while stack and stack[-1] <= x:
            y = stack.pop()
            if not stack or stack[-1] > x:
                res += y * x
            else:
                res += stack[-1] * y
        stack.append(x)
    while len(stack) >= 2:
        x = stack.pop()
        res += stack[-1] * x
    return res
