def dfs(graph,node,visited):
    visited[node]=True
    print(node,end='  ')
    for i in graph[node]:
        if not visited[node]:
            dfs(graph,i,visited)

graph=[ [],
        [2,3,8],
        [1,7],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
]
visited=[False]* 9
dfs(graph,1,visited)