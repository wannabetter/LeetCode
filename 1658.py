from typing import List


def minOperations(nums: List[int], x: int) -> int:
    n = len(nums)
    total = sum(nums)

    if total < x:
        return -1

    right, lSum, rSum, ans = 0, 0, total, n + 1
    for left in range(-1, n - 1):
        if left != -1:
            lSum += nums[left]
        while right < n and lSum + rSum > x:
            rSum -= nums[right]
            right += 1
        if lSum + rSum == x:
            ans = min(ans, left + 1 + n - right)
    return -1 if ans > n else ans
