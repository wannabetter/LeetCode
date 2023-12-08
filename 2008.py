import bisect
from typing import List


def maxTaxiEarnings(n: int, rides: List[List[int]]) -> int:
    rides.sort(key=lambda r:r[1])
    m = len(rides)
    dp = [0] * (m+1)
    for i in range(m):
        j = bisect.bisect_right(rides,rides[i][0],hi=i,key=lambda r:r[1])
        dp[i + 1] = max(dp[i], dp[j] + rides[i][1] - rides[i][0] + rides[i][2])
    return dp[m]