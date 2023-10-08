from heapq import heappush, heappop


class StockPrice:

    def __init__(self):
        self.dict = dict()
        self.maxi = []
        self.mini = []
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        self.dict[timestamp] = price
        self.cur = max(self.cur, timestamp)
        heappush(self.maxi, (-price, timestamp))
        heappush(self.mini, (price, timestamp))

    def current(self) -> int:
        return self.dict[self.cur]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxi[0]
            if -price == self.dict[timestamp]:
                return -price
            heappop(self.maxi)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.mini[0]
            if price == self.dict[timestamp]:
                return price
            heappop(self.mini)
