from typing import List


def minMaxGame(nums: List[int]) -> int:
    while len(nums) != 1:
        newNums = [0 for _ in range(len(nums) // 2)]
        for index in range(len(newNums)):
            if index % 2 == 0:
                newNums[index] = min(nums[2 * index], nums[2 * index + 1])
            else:
                newNums[index] = max(nums[2 * index], nums[2 * index + 1])
        nums = newNums
    return nums[-1]