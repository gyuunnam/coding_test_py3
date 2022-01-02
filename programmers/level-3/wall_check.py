#https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations
def solution(n, weak, dist):
    #n은 외벅의 길이,weak은 취약지점 위치 배열, dist는 1시간동안 이동 가능거리 배열
    #목적:취약지점을 최소의 인원으로 처리한 결과를 배출
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist)+1
    
    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            count=1
            position=weak[start]+friends[count-1]
            for index in range(start,start+length):
                if position<weak[index]:
                    count+=1
                    if count> len(dist):
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer