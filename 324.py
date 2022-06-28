import math
from typing import List


def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return

    nums.sort(reverse=True)
    for item in nums[0:math.ceil(len(nums) / 2)]:
        nums.pop(0)
        nums.append(item)

    indexList = [index for index in range(math.ceil(len(nums) / 2), len(nums))]
    indexList.append(-1)

    index = 0
    while index < len(nums):
        num = nums.pop(indexList.pop(0))
        if num == -1:
            break
        nums.insert(index + 1, num)
        index = index + 2

    print(nums)


if __name__ == "__main__":
    wiggleSort([6, 1, 2, 4, 4, 4])
