def minAddToMakeValid(s: str) -> int:
    QueueLeft, QueueRight = [], []
    for Char in s:
        if Char == "(":
            QueueLeft.append(Char)
        else:
            if len(QueueLeft) == 0:
                QueueRight.append(Char)
            else:
                QueueLeft.pop()
    return len(QueueLeft)+len(QueueRight)