from itertools import combinations
n=int(input())
m=int(input())
chicken,house=[],[]
for r in range(n):
    data=list(map(int,input().split()))
    for c in range(n):
        house.append((r,c))
    else:
        chicken.append((r,c))

candidates=list(combinations(chicken,m))

def get_sum(candidate):
    res=0
    for hx,hy in house:
        temp=1e9
        for cx,cy in candidate:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        res+=temp
    return res
res=1e9
for candidate in candidates:
    res=min(res,get_sum(candidate))
print(res)