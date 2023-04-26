from typing import List


def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
    arr = [0]
    for index, num in enumerate(nums):
        arr.append(arr[-1] + num)
    res = maxA = maxB = 0
    for index in range(firstLen + secondLen, len(arr)):
        maxA = max(maxA, arr[index - secondLen] - arr[index - secondLen - firstLen])
        maxB = max(maxB, arr[index - firstLen] - arr[index - firstLen - secondLen])
        res = max(res, maxA + arr[index] - arr[index - secondLen], maxB + arr[index] - arr[index - firstLen])
    return res
