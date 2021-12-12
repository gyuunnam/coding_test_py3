#https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    bucket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer.append(bucket.pop())
                    bucket.pop()
                    #bucket = bucket[:-2]
                break
    return len(answer)*2