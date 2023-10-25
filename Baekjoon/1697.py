import sys
from collections import deque

# 5
# -> 4, 6, 10
# -> 3, 5, 8, 5, 7, 12, 9, 11, 20
# -> 2, 4, 6 // 4, 6, 10 // 7, 9, 16 // 4, 6, 10 // 6, 8, 14 // 11, 13 , 22 // 8, 10, 18 // ...
# -> 17


MAX = 100000
n, k = map(int, input().split())
ans = [ MAX for _ in range(MAX+1)]

queue = deque()
queue.append(n)
ans[n] = 0

while queue:
    now = queue.popleft()
    if now == k:
        break
    # if now - 1 < 0 or now * 2 > 100000:
    #     continue
    for nx in (now-1, now+1, now*2) :
        if nx < 0 or nx > 100000:
            continue
        if not ans[nx] != MAX :
            ans[nx] = ans[now] + 1
            queue.append(nx)

print(ans[k])