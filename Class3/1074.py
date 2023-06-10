import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

res = 0
l = 2 ** (n-1) # 한 사분면의 길이

# 길이가 0이 되면 종료
while l: 
    if c // l < 1:
        if r // l >= 1: # 3사분면
            res += 2 * l * l
    else:
        if r // l < 1: # 1사분면
            res += l * l
        else: # 4사분면
            res += 3 * l * l
    # 해당하는 구역을 다시 분할
    c %= l
    r %= l
    l //= 2

print(res)