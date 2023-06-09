import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for item in range(1, n+1):
        result *= item
    return result

# 입력값으로 주어진 팩토리얼을 계산하여 숫자 리스트로 변환
n = list(map(int, str(factorial(int(input())))))

count = 0

# 뒤에서부터 숫자를 탐색하면서 0의 개수를 세기 위한 반복문
for i in reversed(n):
    if not i:
        count += 1
    else:
        print(count)  # 처음으로 0이 아닌 숫자가 나왔을 때 0의 개수를 출력
        break
