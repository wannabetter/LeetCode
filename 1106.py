def parseBoolExpr(expression: str) -> bool:  # expression = "|(&(t,f,t),!(t))"
    Stack = []
    for exp in expression:
        if exp == ",":
            continue
        if exp != ")":
            Stack.append(exp)
        TrueNum, FalseNum = 0, 0
        while Stack[-1] != "(":
            Temp = Stack.pop()
            if Temp == "t":
                TrueNum += 1
            if Temp == 'f':
                FalseNum += 1
        Stack.pop()
        if Stack[-1] == "|":
            Stack.append("t" if TrueNum != 0 else "f")
        elif Stack[-1] == "&":
            Stack.append("f" if FalseNum != 0 else "t")
        else:
            Stack.append("f" if FalseNum == 0 else "t")
        Stack.pop()