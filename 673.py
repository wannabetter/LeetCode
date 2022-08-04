from typing import List


def findNumberOfLIS(nums: List[int]) -> int:
    DP = [0] * len(nums)
    Cnt = [0] * len(nums)
    MaxLen, ans = 0, 0
    for IndexI, num in enumerate(nums):
        DP[IndexI] = 1
        Cnt[IndexI] = 1
        for IndexJ in range(IndexI):
            if num > nums[IndexJ]:
                if DP[IndexJ] + 1 > DP[IndexI]:
                    DP[IndexI] = DP[IndexJ] + 1
                    Cnt[IndexI] = Cnt[IndexJ]
                elif DP[IndexJ] + 1 == DP[IndexI]:
                    Cnt[IndexI] += Cnt[IndexJ]
        if DP[IndexI] > MaxLen:
            MaxLen = DP[IndexI]
            ans = Cnt[IndexI]
        elif DP[IndexI] == MaxLen:
            ans += Cnt[IndexI]
    return ans


if __name__ == "__main__":
    print(findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
