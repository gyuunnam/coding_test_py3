def solution(triangle):
    answer = 0
    if len(triangle)>0:
        triangle[1][0]+=triangle[0][0]
        triangle[1][1]+=triangle[0][0]
    if len(triangle)>2:
        for i in range(2,len(triangle)):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1]+=triangle[i-1][-1]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
                #print(triangle[i][j],end=" ")
            #print()
            
    answer=max(triangle[-1])
    return answer