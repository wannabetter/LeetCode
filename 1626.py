from typing import List


def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    players = sorted(zip(scores, ages))
    dp = [0] * len(scores)
    ans = 0
    for i in range(len(scores)):
        for j in range(i):
            if players[i][1] >= players[j][1]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += players[i][0]
        ans = max(ans, dp[i])
    return ans
