from typing import List


def maxAbsoluteSum(nums: List[int]) -> int:
    ans = 0
    pre_sum = [0]
    max_index, min_index = 0, 0
    for index, num in enumerate(nums):
        pre_sum.append(num + pre_sum[-1])
        if pre_sum[-1] > 0:
            ans = max(abs(pre_sum[-1] - pre_sum[min_index]), ans)
        else:
            ans = max(abs(pre_sum[-1] - pre_sum[max_index]), ans)
        if pre_sum[-1] > pre_sum[max_index]:
            max_index = index + 1
        if pre_sum[-1] < pre_sum[min_index]:
            min_index = index + 1
    return ans