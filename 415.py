def addStrings(num1: str, num2: str) -> str:
    ans = ""
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    c = 0
    index1, index2 = len(num1) - 1, len(num2) - 1
    while index1 >= 0 and index2 >= 0:
        if int(num1[index1]) + int(num2[index2]) + c > 9:
            ans = str((int(num1[index1]) + int(num2[index2]) + c) % 10) + ans
            c = 1
        else:
            ans = str(int(num1[index1]) + int(num2[index2]) + c) + ans
            c = 0
        index1 -= 1
        index2 -= 1
    while index1 >= 0:
        if int(num1[index1]) + c > 9:
            ans = str((int(num1[index1]) + c) % 10) + ans
            c = 1
        else:
            ans = str(int(num1[index1]) + c) + ans
            c = 0
        index1 -= 1
    while index2 >= 0:
        if int(num2[index2]) + c > 9:
            ans = str((int(num2[index2]) + c) % 10) + ans
            c = 1
        else:
            ans = str(int(num2[index2]) + c) + ans
            c = 0
        index2 -= 1
    if c == 1:
        ans = "1" + ans
    return ans
