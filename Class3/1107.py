import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - n)

for nums in range(1000001):
    num = str(nums)

    for i in range(len(num)):
        if int(num[i]) in broken:
            break
    else:
        min_count = min(min_count, abs(int(num) - n) + len(num))

print(min_count)