import sys
input = sys.stdin.readline

n = int(input())
cmd = [input() for _ in range(n)]
queue = []

for c in cmd:
    if 'push' in c.split()[0]:
        queue.append(c.split()[1])
    elif 'pop' in c:
        print(queue.pop(0)) if queue else print(-1)
    elif 'size' in c:
        print(len(queue))
    elif 'empty' in c:
        print(0) if queue else print(1)
    elif 'front' in c:
        print(queue[0]) if queue else print(-1)
    elif 'back' in c:
        print(queue[-1]) if queue else print(-1)