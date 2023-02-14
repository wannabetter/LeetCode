from typing import List


# 前缀和+单调栈
def longestWPI(hours: List[int]) -> int:
    stack = [0]
    arrSum = [0] * (len(hours) + 1)
    for j, hour in enumerate(hours, 1):
        arrSum[j] = arrSum[j - 1] + (1 if hour > 8 else -1)
        if arrSum[j] < arrSum[stack[-1]]:
            stack.append(j)
    res = 0
    for i in range(len(hours), 0, -1):
        while stack and arrSum[i] > arrSum[stack[-1]]:
            res = max(res, i - stack.pop())
    return res
