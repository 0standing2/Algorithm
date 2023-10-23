import sys
from collections import deque


def dfs(now):
    visited[now] = True
    print(now, end=" ")

    for i in graph[now]:
        if not visited[i]:
            dfs(i)

def bfs(now) :
    queue = deque([now])
    visited[now] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in graph[now] :
            if not visited[i]:
                visited[i] = True
                queue.append(i)




n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
q = deque([])

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1) :
    graph[i].sort()

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)