def solution(n, computers):
    answer = 0
    def dfs(x,y):
        if x<=-1 or y<=-1 or x>=len(computers[0]) or y>=len(computers):
            return False
        if computers[x][y]==1:
            computers[x][y]=0
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            return True
        return False
            
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if dfs(i,j):
                answer+=1
                
    return answer