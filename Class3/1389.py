import sys
input = sys.stdin.readline

def dfs(count, start, end):
    visited[u] = True
    count += 1
    for s in network[start]:
        if visited[end]:
            return count
        if not visited[end]:
            print(count, s, end)
            print(visited[end])
            dfs(count, s, end)

n, m = map(int, input().split())

network = {}
visited = [False for _ in range(n)]
res = 9999999

# 입력
for _ in range(m):
    u, v = map(int, input().split())
    if u in network:
        network[u].append(v)
    else:
        network[u] = [v]
    if v in network:
        network[v].append(u)
    else:
        network[v] = [u]

print(network)

for start in range(1, n+1):
    sum = 0
    for end in range(1, n+1):
        count = 0
        sum += dfs(count, start, end)
    if sum < res:
        res = sum
        
print(res)