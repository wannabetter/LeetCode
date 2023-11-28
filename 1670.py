class FrontMiddleBackQueue:

    def __init__(self):
        self.n = 0
        self.arr = list()

    def pushFront(self, val: int) -> None:
        self.n = self.n + 1
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.arr.insert(self.n // 2, val)
        self.n = self.n + 1

    def pushBack(self, val: int) -> None:
        self.n = self.n + 1
        self.arr.append(val)

    def popFront(self) -> int:
        if self.n == 0:
            return -1
        ans = self.arr.pop(0)
        self.n = self.n - 1
        return ans

    def popMiddle(self) -> int:
        if self.n == 0:
            return -1
        ans = self.arr.pop(self.n//2 - 1 if self.n%2==0 else self.n//2)
        self.n = self.n - 1
        return ans

    def popBack(self) -> int:
        if self.n == 0:
            return -1
        ans = self.arr.pop()
        self.n = self.n - 1
        return ans