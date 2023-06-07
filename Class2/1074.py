import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

array_size = 2 ** (2*n)
half = 2 ** n-1

if r < half and c < half:
    start = 0
elif r < half and c >= half:
    start = 1/4 * array_size
elif r >= half and c < half:
    start = 2/4 * array_size
elif r >= half and c >= half:
    start = 3/4 * array_size


