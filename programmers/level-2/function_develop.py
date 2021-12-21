import math

def solution(progresses, speeds):
    answer = []
    rest = []
    temp = []

    size = len(progresses)

    for i in progresses:
        rest.append(100 - i)

    for i in range(size):
        temp.append(math.ceil(rest[i] / speeds[i]))

    cnt = 0
    p = temp[0]
    for i in range(len(temp)):
        if p < temp[i]:
            answer.append(cnt)
            p = temp[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)


    return answer