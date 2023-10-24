import sys
from collections import deque

dx = [ 1, -1, 0, 0]
dy = [ 0, 0, -1, 1]



def bfs() :
    queue = deque()
    queue.append((0,0))
    ans[0][0] = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # print("now : ", nx, " ", ny)
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 1 and ans[nx][ny] == 0:
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx, ny))
                # print(ans[nx][ny])

n, m = map(int, input().split())
ans = [ [0 for _ in range(m+1)] for _ in range(n+1)]
graph = []


for _ in range(n):
    graph.append(list(map(int, input())))


bfs()
print(ans[n-1][m-1])