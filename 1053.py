from typing import List


def prevPermOpt1(arr: List[int]) -> List[int]:
    i = len(arr) - 2
    j = len(arr) - 1
    temp = 0
    tempJ = -1
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i == -1:
        return arr
    while j > i:
        if arr[i] > arr[j] >= temp:  # arr[j]>=temp 这样才能保证最左边
            temp = arr[j]
            tempJ = j
        j -= 1
    arr[tempJ], arr[i] = arr[i], arr[tempJ]
    return arr
