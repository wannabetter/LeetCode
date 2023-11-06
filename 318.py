from typing import List


def maxProduct(words: List[str]) -> int:
    ans = 0
    masks = [0] * len(words)
    for index, word in enumerate(words):
        for c in word:
            masks[index] |= 1 << (ord(c) - ord('a'))
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            if masks[i] & masks[j] == 0:
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans

