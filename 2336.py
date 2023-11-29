from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.set = set()
        self.heap = [1]

    def popSmallest(self) -> int:
        pop = heappop(self.heap)
        if not self.heap:
            heappush(self.heap, pop + 1)
        self.set.add(pop)
        return pop

    def addBack(self, num: int) -> None:
        if num in self.set:
            heappush(self.heap,num)
            self.set.remove(num)
