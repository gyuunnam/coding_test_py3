#https://programmers.co.kr/learn/courses/30/lessons/81303
from collections import defaultdict


def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    linked_list = defaultdict(list)

    for i in range(1, n + 1):
        linked_list[i].append(i - 1)
        linked_list[i].append(i + 1)

    stack = []
    k += 1

    for line in cmd:
        if line[0] == "D":
            for _ in range(int(line[2:])):
                k = linked_list[k][1]

        elif line[0] == "U":
            for _ in range(int(line[2:])):
                k = linked_list[k][0]
                
        elif line[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            answer[k - 1] = "X"

            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif line[0] == "Z":
            prev, next, now = stack.pop()
            answer[now - 1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(answer)