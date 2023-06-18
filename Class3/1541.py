import sys
input = sys.stdin.readline

exp = input().split('-')
lst = []

for e in exp:
    sum = 0
    plus = e.split('+')
    for p in plus:
        sum += int(p)
    lst.append(sum)
    
res = lst[0]
for i in range(1, len(lst)):
    res -= lst[i]
print(res)