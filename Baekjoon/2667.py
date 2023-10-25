import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = []

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny<0 or ny >= n:
                continue
            # print(nx, ny)
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())
graph = []
visited = [[False for _ in range(n+1)] for _ in range(n+1)]


for _ in range(n) :
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for i in range(len(ans)) :
    print(ans[i])
