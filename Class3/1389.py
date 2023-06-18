import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    count = [0 for _ in range(n+1)]
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        vertices = queue.popleft()
        for v in graph[vertices]:
            if v not in visited:
                count[v] += count[vertices] + 1
                visited.append(v)
                queue.append(v)
    return sum(count)

n, m = map(int, input().split())
graph = {}

for _ in range(m):
    u, v = map(int, input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

res = []
for i in range(1, n+1):
    res.append(bfs(i))

print(res.index(min(res))+1)