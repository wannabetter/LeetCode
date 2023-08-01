from typing import List


def sumOfPower(nums: List[int]) -> int:
    ans = 0
    nums.sort()
    mod = 10 ** 9 + 7
    dp = [0 for _ in range(len(nums))]
    pre_sum = [0 for _ in range(len(nums) + 1)]
    for index in range(len(nums)):
        dp[index] = (nums[index] + pre_sum[index]) % mod
        pre_sum[index + 1] = (pre_sum[index] + dp[index]) % mod
        ans = (ans + nums[index] * nums[index] * dp[index]) % mod
    return ans
