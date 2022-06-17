from typing import List


def findPairs(nums: List[int], k: int) -> int:
    Sum = 0
    Left_Last = -1
    Right = 0
    nums.sort()

    for Left in range(len(nums)):
        Right = max(Right, Left + 1)
        while Right < len(nums) and nums[Right] - nums[Left] < k:
            Right = Right + 1
        if Right < len(nums) and nums[Right] - nums[Left] == k:
            if Left_Last < 0 or nums[Left_Last] != nums[Left]:
                Left_Last = Left
                Sum = Sum + 1

    return Sum


if __name__ == "__main__":
    print(findPairs([1, 3, 1, 5, 4], 0))
