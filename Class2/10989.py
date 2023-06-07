import sys
input = sys.stdin.readline

lst = [0] * 10001

for _ in range(int(input())):
    lst[int(input())] += 1

for i in range(10001):
    if lst[i]: 
        for j in range(lst[i]):
            print("".join(str(i)))