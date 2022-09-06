from collections import defaultdict


def uniqueLetterString(s: str) -> int:
    Res = 0
    Index = defaultdict(list)

    for index, char in enumerate(s):
        Index[char].append(index)
    print(Index)
    for arr in Index.values():
        arr = [-1] + arr + [len(s)]
        for index in range(1, len(arr) - 1):
            Res += (arr[index] - arr[index - 1]) * (arr[index + 1] - arr[index])

    return Res
