from collections import defaultdict


def maxLengthBetweenEqualCharacters(s: str) -> int:
    Dicts = defaultdict(list)
    Max = -1
    for Index, Char in enumerate(s):
        Dicts[Char].append(Index)

    for key in Dicts:
        Max = max(Dicts[key][-1] - Dicts[key][0] - 1, Max)

    return Max


if __name__ == '__main__':
    print(maxLengthBetweenEqualCharacters("abca"))
