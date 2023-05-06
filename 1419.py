from collections import Counter


def minNumberOfFrogs(croakOfFrogs: str) -> int:
    cnt = Counter()
    for char in croakOfFrogs:
        cnt[char] += 1
        if char == 'c':
            if cnt['k'] > 0: cnt['k'] -= 1
        elif char == 'r':
            if cnt['c'] == 0: return -1
            cnt['c'] -= 1
        elif char == 'o':
            if cnt['r'] == 0: return -1
            cnt['r'] -= 1
        elif char == 'a':
            if cnt['o'] == 0: return -1
            cnt['o'] -= 1
        else:
            if cnt['a'] == 0: return -1
            cnt['a'] -= 1
    return -1 if cnt['c'] + cnt['r'] + cnt['o'] + cnt['a'] > 0 else cnt['k']
