from collections import Counter


def digitCount(num: str) -> bool:
    cnt = Counter(num)
    print(cnt)
    for index, char in enumerate(num):
        if cnt[str(index)] != int(char):
            return False
    return True