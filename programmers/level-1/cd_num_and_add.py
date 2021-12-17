import math
def num_cnt(num):
    cnt=0
    for i in range(1,num//2+1):
        if num%i==0:
            cnt+=1
            
    if cnt%2==1:
        return num
    else:
        return -num
    
def solution(left, right):
    answer = 0
    for n in range(left,right+1):
        answer+=num_cnt(n)
    return answer