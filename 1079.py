from collections import Counter


def numTilePossibilities(tiles: str) -> int:
    cnt = Counter(tiles)
    chars = set(tiles)

    def DFS(index):
        if index == 0:
            return 1
        res = 1
        for char in chars:
            if cnt[char] > 0:
                cnt[char] -= 1
                res += DFS(index - 1)
                cnt[char] += 1
        return res

    return DFS(len(tiles))-1
