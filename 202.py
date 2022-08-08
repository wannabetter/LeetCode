from collections import Counter


def isHappy(n: int) -> bool:
    Cnt = Counter()

    def Get_Num(num):
        Sum = 0
        while num:
            Sum = Sum + (num % 10) ** 2
            num = num // 10
        return Sum

    while True:
        if n == 1:
            return True
        if Cnt[n] == 1:
            return False
        Cnt[n] += 1
        n = Get_Num(n)
