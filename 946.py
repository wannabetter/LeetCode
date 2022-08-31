from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    Queue = []
    while popped:
        flag = True
        target = popped.pop(0)
        if target in Queue:
            while Queue:
                temp = Queue.pop()
                if temp == target:
                    flag = False
                    break
        if target in pushed:
            while pushed:
                temp = pushed.pop(0)
                Queue.append(temp)
                if temp == target:
                    flag = False
                    Queue.pop()
                    break
        if flag:
            return False
    return True
