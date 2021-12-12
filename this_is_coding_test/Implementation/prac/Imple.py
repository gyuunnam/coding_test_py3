n=int(input())
x,y=1,1
plans=input().split()


way={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
for plan in plans:
    if plan in way:
        nx=x+way[plan][0]
        ny=y+way[plan][1]
    if nx<1 or ny <1 or nx >n or ny>n:
        continue
    x,y=nx,ny

print(x,y)