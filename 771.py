from collections import Counter


def numJewelsInStones(jewels: str, stones: str) -> int:
    ans = 0
    cnt = Counter(stones)
    for jewel in jewels:
        ans += cnt[jewel]
    return ans
