class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seen = set()
        self.dict = {}
        self.index = 0

    def get(self, key: int) -> int:
        if key not in self.seen:
            return -1
        else:
            ans = self.dict[key][0]
            self.dict[key] = (ans,self.index)
            self.index = self.index + 1
            return ans

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            self.dict[key] = (value,self.index)
            self.index = self.index + 1
            return
        if len(self.seen) < self.capacity:
            self.seen.add(key)
            self.dict[key] = (value,self.index)
            self.index = self.index + 1
        else:
            dummy,index = -1,self.index
            for se in self.seen:
                if self.dict[se][1] < index:
                    dummy = se
                    index = self.dict[se][1]
            del self.dict[dummy]
            self.seen.remove(dummy)
            self.dict[key] = (value,self.index)
            self.seen.add(key)
            self.index = self.index + 1