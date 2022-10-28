from math import inf
from typing import List


def sumSubarrayMins(arr: List[int]) -> int:
    Stack, Left, Right = [], [0] * len(arr), [0] * len(arr)
    for index, num in enumerate(arr):
        while Stack and num <= arr[Stack[-1]]:
            Stack.pop()
        Left[index] = index - (Stack[-1] if Stack else -1)
        Stack.append(index)
    Stack = []
    for index in range(len(arr) - 1, -1, -1):
        while Stack and arr[index] < arr[Stack[-1]]:
            Stack.pop()
        Right[index] = (Stack[-1] if Stack else len(arr)) - index
        Stack.append(index)
    Res = 0
    for L, R, X in zip(Left, Right, arr):
        Res += L * R * X
    return Res % (10 ** 9 + 7)
