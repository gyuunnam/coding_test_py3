#https://programmers.co.kr/learn/courses/30/lessons/42579

import heapq
from collections import defaultdict
def solution(genres, plays):
    answer = []
    gen_play=[]
    sorted_index=[]
    sorted_genres=[]
    sorted_plays=[]
    all_gen=defaultdict(int)
    for i in range(len(plays)):
        heapq.heappush(gen_play,(-plays[i],(i,genres[i],plays[i])))
        all_gen[genres[i]]+=plays[i]
    
    for _ in range(len(plays)):
        _,sums =heapq.heappop(gen_play)
        sorted_index.append(sums[0])
        sorted_genres.append(sums[1])
        sorted_plays.append(sums[2])
    max_keys=sorted(all_gen,key=lambda x:all_gen[x])
    while max_keys:
        max_key=max_keys.pop()
        cnt=0
        for i in range(len(genres)):
            if cnt==2:break
            if sorted_genres[i]==max_key:
                answer.append(sorted_index[i])
                cnt+=1

    return answer