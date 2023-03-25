from typing import List


def findLengthOfShortestSubarray(arr: List[int]) -> int:
    n = len(arr)
    right = n - 1
    while right and arr[right - 1] <= arr[right]:
        right -= 1
    if right == 0:
        return 0
    ans = right
    left = 0
    while left == 0 or arr[left - 1] <= arr[left]:
        while right < n and arr[left] > arr[right]:
            right += 1
        ans = min(ans, right - left - 1)
        left += 1
    return ans
