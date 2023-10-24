import sys
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n) :
    graph[i].sort()

queue = deque()
queue.append(1)
visited[1] = True

cnt = 0
while queue:
    x = queue.popleft()
    for i in range(len(graph[x])):
        if not visited[graph[x][i]]:
            cnt += 1
            visited[graph[x][i]] = True
            queue.append(graph[x][i])

print(cnt)
