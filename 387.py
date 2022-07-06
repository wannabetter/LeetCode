from collections import Counter


def firstUniqChar(s: str) -> int:
    cnt = Counter(s)
    for index, char in enumerate(s):
        if cnt[char] == 1:
            return index
    return -1


if __name__ == "__main__":
    firstUniqChar("leetcode")
