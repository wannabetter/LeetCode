from typing import List


def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
    n = len(s)
    count = [0] * (n + 1)
    for index in range(n):
        count[index + 1] = count[index] ^ (1 << ord(s[index]) - ord('a'))
    ans = []
    for left, right, k in queries:
        bits = (count[right + 1] ^ count[left]).bit_count()
        ans.append(bits <= 2 * k + 1)
    return ans
