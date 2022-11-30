from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.MaxFreq = 0
        self.Freq = defaultdict(int)
        self.Group = defaultdict(list)

    def push(self, val: int) -> None:
        self.Freq[val] += 1
        self.Group[self.Freq[val]].append(val)
        self.MaxFreq = max(self.MaxFreq, self.Freq[val])

    def pop(self) -> int:
        Val = self.Group[self.MaxFreq].pop()
        self.Freq[Val] -= 1
        if len(self.Group[self.MaxFreq]) == 0:
            self.MaxFreq -= 1
        return Val
