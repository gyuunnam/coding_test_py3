import deque
def bfs(graph,node,visited):
    queue=depue([node])
    visited[node]=True

    while queue:
        pop=queue.popleft()
        print(pop,end='  ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True





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
bfs(graph,1,visited)