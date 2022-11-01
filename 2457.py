from typing import List


def makeIntegerBeautiful(n: int, target: int) -> int:
    Tail = 1
    while True:
        Temp = Num = n + (Tail - n % Tail) % Tail  # 有一种特殊情况，比如n个位是0，模10之后又是0，Tail-0还是等与Tail，再模一个Tail就等于0
        # 防止进位，这样做可以防止不该进位的时候进位
        S = 0
        while Num:
            S += Num % 10
            Num = Num // 10
        if S <= target:
            return Temp - n
        Tail *= 10
