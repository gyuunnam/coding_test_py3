#https://programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    answer = 0
    dp=[i for i in range(n+1)]
    dp[1]=1
    dp[2]=2
    #dp[3]=3
    #dp[4]=5
    #dp[5]=8
    if n<2:
        return dp[n]
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2]) % 1000000007
    return dp[n]