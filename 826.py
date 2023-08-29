from typing import List


def numFactoredBinaryTrees(arr: List[int]) -> int:
    ans = 0
    dp = [1] * len(arr)
    arr = sorted(arr)

    for index in range(len(arr)):
        left, right = 0, index - 1
        while left <= right:
            while left <= right and arr[left] * arr[right] > arr[index]:
                right = right - 1
            if left <= right and arr[left] * arr[right] == arr[index]:
                if left != right:
                    dp[index] = (dp[index] + dp[left] * dp[right] * 2) % (10 ** 9 + 7)
                else:
                    dp[index] = (dp[index] + dp[left] * dp[right]) % (10 ** 9 + 7)
            left = left + 1
        ans = (ans + dp[index]) % (10 ** 9 + 7)
    return ans
