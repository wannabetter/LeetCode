def scoreOfParentheses(s: str) -> int:
    Stack = [0]
    for Char in s:
        if Char == '(':
            Stack.append(0)
        else:
            v = Stack.pop()
            Stack[-1] += max(2 * v, 1)
        print(Stack)
    return Stack[-1]

