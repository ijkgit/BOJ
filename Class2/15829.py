import sys
input = sys.stdin.readline

# input
l = int(input())
lst = list(input().strip())
h = 0

# for rule
for i, v in enumerate(lst):
    lst[i] = ord(v) - 96

# hash function
for i, v in enumerate(lst):
    h += v * (31 ** i)

# result
print(h%1234567891)