from math import inf


class StockSpanner:

    def __init__(self):
        self.Idx = -1
        self.Stack = [(-1, inf)]

    def next(self, price: int) -> int:
        self.Idx += 1
        while price >= self.Stack[-1][1]:
            self.Stack.pop()
        self.Stack.append((self.Idx, price))
        print(self.Stack)
        return self.Idx - self.Stack[-2][0]


if __name__ == '__main__':
    S = StockSpanner()
    print(S.next(100))
    print(S.next(80))
    print(S.next(60))
    print(S.next(70))
    print(S.next(60))
    print(S.next(75))
    print(S.next(85))
