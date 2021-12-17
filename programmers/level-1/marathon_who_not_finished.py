from collections import defaultdict
def solution(participant, completion):
    answer = ''
    stat=defaultdict(int)
    for name in participant:
        stat[name]+=1
    for name in completion:
        stat[name]-=1
    for name in stat:
        if stat[name]>0:
            answer=name
    return answer