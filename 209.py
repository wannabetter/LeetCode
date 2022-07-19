from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    if not nums:
        return 0

    Start, End, Total, Res = 0, 0, 0, len(nums) + 1
    while End < len(nums):
        Total += nums[End]
        while Start < len(nums) and Total >= target:
            Res = min(Res, End - Start + 1)
            Total = Total - nums[Start]
            Start = Start + 1
        End = End + 1

    return 0 if Res == len(nums) + 1 else Res


if __name__ == "__main__":
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
