from typing import List


def canJump(nums: List[int]) -> bool:
    MaxJump = 0
    for Index, Jump in enumerate(nums):
        if Index <= MaxJump <= Index + Jump:
            MaxJump = max(Index + Jump, MaxJump)
    return MaxJump >= len(nums)


if __name__ == "__main__":
    print(canJump(nums=[0, 2, 3]))
