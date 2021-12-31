#https://programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict
import math
def solution(enroll, referral, seller, amount):
    answer = []
    #center이익금=SUM(해당자의 이익금*(0.1)^거리)
    #enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]             => enroll길이가 총 조직 구성원 수, 조직 참여 순서
    #referel=[ "-",   "-",    "mary", "edward", "mary", "mary", "jaimie", "edward"]         => referral
    #seller=["young", "john", "tod", "emily", "mary"]                                       => 누가 팔았냐
    #amout=[12, 4, 2, 5, 10]                                                                 => seller가 얼마나 팔았냐
    enr_ref={}
    enr_sum=defaultdict(int)
    for i in range(len(enroll)):
        enr_ref[enroll[i]]=referral[i]
    
    for i in range(len(amount)):  
        now=seller[i]
        prev=enr_ref[now]
        enr_sum[seller[i]]+=(100*amount[i])
        temp_val=100*amount[i]
        #cnt=1
        while True:
            #val=100*amount[i]*(0.1**(cnt))
            val=temp_val*0.1
            profit=int(val) if val>=1 else 0
            if profit==0:break
            enr_sum[now]-=profit 
            enr_sum[prev]+=profit
            #cnt+=1
            #print(now,"==",prev,"=>",profit,end=" ")
            if prev=="-":break
            temp_val=val
            now=prev
            prev=enr_ref[prev]
        #print()
    #for i in range(len(seller)):
    for ele in enroll:
        answer.append(enr_sum[ele])
    return answer