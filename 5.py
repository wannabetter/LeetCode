# 费了九牛二虎之力终于把这个题给做上了，解析写的太复杂了，让人看不懂，总结就是回文串长度1，2要单独考虑，因为用动态规划的时候
# aba 让左右都减去a，只剩下一个，如果是abba，左右都减去a，剩下两个，所有说1和2的情况单独考虑，其他的用转移方程

def longestPalindrome(s: str) -> str:
    Res = s[0]
    MaxLen = 1
    DP = [[False] * len(s) for _ in range(len(s))]
    for Index in range(len(s)):
        DP[Index][Index] = True
        if Index != 0 and s[Index] == s[Index - 1]:
            DP[Index][Index - 1] = DP[Index - 1][Index] = True
            MaxLen = 2
            Res = s[Index - 1:Index + MaxLen - 1]
        else:
            DP[Index][Index - 1] = DP[Index - 1][Index] = False

    for IndexI in range(len(s)):
        for IndexJ in range(IndexI):
            if IndexI - IndexJ >= 2:
                DP[IndexI][IndexJ] = DP[IndexI - 1][IndexJ + 1] and s[IndexI] == s[IndexJ]
                if DP[IndexI][IndexJ] and IndexI - IndexJ + 1 > MaxLen:
                    MaxLen = IndexI - IndexJ + 1
                    Res = s[IndexJ:IndexJ+MaxLen]

    return Res


if __name__ == "__main__":
    print(longestPalindrome("caba"))
