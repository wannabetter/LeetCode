from typing import List


def maxSubArray(nums: List[int]) -> int:
    dp = [nums[0]]
    for index in range(1, len(nums)):
        dp.append(max(dp[index - 1] + nums[index], nums[index]))
    return max(dp)


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
