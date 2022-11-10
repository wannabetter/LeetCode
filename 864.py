from typing import List
from collections import defaultdict


def shortestPathAllKeys(grid: List[str]) -> int:
    Keys, Dists, Queue = 0, defaultdict(lambda: 0x3f3f3f3f), []
    for IndexI, Chars in enumerate(grid):
        for IndexJ, Char in enumerate(Chars):
            if Char == "@":
                Queue.append((IndexI, IndexJ, 0))
                Dists[(IndexI, IndexJ, 0)] = 0
            if 'a' <= Char <= 'z':
                Keys += 1
    while Queue:
        X, Y, Cur = Queue.pop(0)
        Step = Dists[(X, Y, Cur)]
        for offSet in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            NewX, NewY = X + offSet[0], Y + offSet[1]
            if NewX < 0 or NewX >= len(grid) or NewY < 0 or NewY >= len(grid[0]):
                continue
            if grid[NewX][NewY] == "#":
                continue
            if "A" <= grid[NewX][NewY] <= 'Z' and (Cur >> (ord(grid[NewX][NewY]) - ord('A')) & 1) == 0:
                continue
            NewCur = Cur
            if "a" <= grid[NewX][NewY] <= 'z':
                NewCur |= (1 << (ord(grid[NewX][NewY]) - ord('a')))
            if NewCur == (1 << Keys) - 1:
                return Step + 1
            if Step + 1 >= Dists[(NewX, NewY, NewCur)]:
                continue
            Dists[(NewX, NewY, NewCur)] = Step + 1
            Queue.append((NewX, NewY, NewCur))
    return -1


if __name__ == '__main__':
    print(shortestPathAllKeys(["@.a..", "###.#", "b.A.B"]))
