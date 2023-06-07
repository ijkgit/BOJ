import sys
input = sys.stdin.readline

n, m = (map(int, input().split()))
lst = list(map(int, input().split()))

start, end = 1, lst[-1]

while start <= end:
    sum = 0
    mid = (start+end) // 2

    for l in lst:
        if l > mid:
            sum += l - mid
    
    if sum < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)