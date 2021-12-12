#https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = [0,0]
    rank=[6,6,5,4,3,2,1]
    cnt=0
    cnts=lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            cnt+=1
    answer[0],answer[1]=rank[cnt+cnts],rank[cnt]

    return answer