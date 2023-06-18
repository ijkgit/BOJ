import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == 1:
            print(count[x])
            break
        if x % 3 == 0:
            nx = x // 3
            if not count[nx]:
                count[nx] = count[x] + 1
                queue.append(nx)
        if x % 2 == 0:
            nx = x // 2
            if not count[nx]:
                count[nx] = count[x] + 1
                queue.append(nx)
        nx = x - 1
        if not count[nx]:
            count[nx] = count[x] + 1
            queue.append(nx)

n = int(input())
count = [0 for _ in range(n+1)]
bfs(n)




