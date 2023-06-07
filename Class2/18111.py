import sys
input = sys.stdin.readline

# 입력
n, m, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 시간, 높이 설정
mintime = sys.maxsize
maxheight = 0

# 최대 높이는 256이므로, 0~256 까지 탐색
for h in range(257):
    tmp = b
    time = 0
    for r in lst:
        for c in r:
            # 현재 좌표의 높이가 목표 높이보다 낮을 때,
            # 블록을 제거하고 인벤토리에 넣어야 한다.
            if c < h:    
                tmp -= (h-c)
                time += 1 * (h-c)
            # 현재 좌표의 높이가 목표 높이보다 높을 때,
            # 인벤토리에서 블록을 꺼내어 쌓아야 한다.
            elif c > h:
                tmp += (c-h)
                time += 2 * (c-h)
	# 인벤토리에 남은 블록 수가 0 이상이고,
	# 현재까지의 시간이 최소 시간보다 작거나 같을 때,
	# 최소 시간과 최대 높이를 갱신한다.
    if tmp >= 0 and mintime >= time:
        mintime = time
        maxheight = h

print(mintime, maxheight)