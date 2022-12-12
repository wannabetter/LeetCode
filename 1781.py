from collections import Counter


def beautySum(s: str) -> int:
    Res = 0
    for IndexI in range(len(s)):
        Max, Cnt = 0, Counter()
        for IndexJ in range(IndexI,len(s))
            Cnt[s[IndexJ]]+=1
            Max=max(Max,Cnt[s[IndexJ]])
            Res+=Max-min(Cnt.values())
    return Res



if __name__ == '__main__':
    print(beautySum('aabcb'))
