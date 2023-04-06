# 其实和转2进制是一个道理，但是问题是-2会出现0 1 -1，当出现-1要res要加他的绝对值，然后n更新为n//(-2)+1,其他都是一样的

def baseNeg2(n: int) -> str:
    if n == 0 or n == 1:
        return str(n)
    res = ""
    while n:
        remain = n % (-2)
        res = str(abs(remain)) + res
        n = n // (-2) + 1 if remain < 0 else n // (-2)
    return res
