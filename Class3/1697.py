import sys
input = sys.stdin.readline

def bfs():
    q = []
    q.append(n)
    while q:
        x = q.pop(0)
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

n, k = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)

bfs()