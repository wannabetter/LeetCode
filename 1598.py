from typing import List


def minOperations(logs: List[str]) -> int:
    Queue = []
    for log in logs:
        print(Queue)
        if log == "../":
            if len(Queue) != 0:
                Queue.pop(0)
        elif log == './':
            continue
        else:
            Queue.append(log)
    return len(Queue)


if __name__ == '__main__':
    print(minOperations(["./", "../", "./"]))
