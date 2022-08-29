from functools import lru_cache
from typing import List


def countRoutes(locations: List[int], start: int, finish: int, fuel: int) -> int:
    @lru_cache(None)
    def DFS(rest, index):
        if abs(locations[index] - locations[finish]) > rest:
            return 0
        
        ans = 0
        for idx in range(len(locations)):
            if idx != index and abs(locations[idx] - locations[index]) <= rest:
                ans += DFS(rest - abs(locations[idx] - locations[index]), idx)

        if index == finish:
            ans += 1
        return ans

    return DFS(fuel, start) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(countRoutes([1, 2, 3], 0, 2, 40))
