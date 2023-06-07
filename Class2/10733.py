import sys
input = sys.stdin.readline

k = int(input())
lst = []

for _ in range(k):
    n = int(input())
    lst.append(n) if n else lst.pop()

print(sum(lst))