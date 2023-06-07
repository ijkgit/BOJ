import sys
input = sys.stdin.readline

# T만큼 반복하여 테스트 데이터를 입력 받음
for _ in range(int(input().rstrip())):
    case = input().rstrip()
    cnt_left, cnt_right, check = 0, 0, 0
    for i in case:
        if i == '(':
            cnt_left += 1
        else:
            cnt_right += 1
            if cnt_right > cnt_left:
                check = 1
    if cnt_left == cnt_right:
        if check: print('NO')
        else: print('YES')
    else: print('NO')