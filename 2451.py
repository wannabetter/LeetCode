from typing import List
from collections import defaultdict


def oddString(words: List[str]) -> str:
    seen = defaultdict(list)
    for word in words:
        chars = list(word)
        temp = 0
        for index, char in enumerate(chars):
            temp = temp * 10 + ord(char) - ord(chars[index - 1])
        seen[temp].append(word)

    for key, items in seen.items():
        if len(items) == 1:
            return items[0]
