from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.flag = [False for _ in range(n)]
        self.stream = [_ for _ in range(n)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        Res = []
        while self.ptr < self.n:
            if type(self.stream[self.ptr]) == int:
                break
            else:
                Res.append(self.stream[self.ptr])
                self.ptr = self.ptr + 1
        return Res
