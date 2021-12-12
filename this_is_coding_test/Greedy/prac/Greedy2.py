n,m=map(int,input().split())
result=0
min_list=[]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
for i in range(n):
    temp=min(data[i])
    result=max(temp,result)

print(result)    
