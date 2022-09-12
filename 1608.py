from typing import List


def specialArray(nums: List[int]) -> int:
    nums.sort()
    Index = 0
    X = len(nums)
    while Index < len(nums):
        if (Index == 0 and X <= nums[Index]) or (nums[Index - 1] < X <= nums[Index]):
            return X
        Index += 1
        X -= 1
    return -1


if __name__ == '__main__':
    print(specialArray([0, 4, 3, 0, 4]))
