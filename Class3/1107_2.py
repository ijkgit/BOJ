import sys
input = sys.stdin.readline
sys.set_int_max_str_digits(10**6)

n = int(input())
m = int(input())
blocked = list(map(int, input().split()))
n_list = list(map(int, str(n)))

start = 100

def plusMinus(start, n):
    return abs(start - n)

def findNum(index, num):
    plus_num = 0
    minus_num = 0
    for i in range (5, 10):
        if i not in blocked:
            plus_num = i
    for i in range (0, 6):
        if i not in blocked:
            minus_num = i
    
    plusCount = plusMinus(plus_num * (10 ** (len(n_list)-index)), int(''.join(map(str, n_list[index:]))))
    minusCount = plusMinus(minus_num * (10 ** (len(n_list)-index)), int(''.join(map(str, n_list[index:]))))
    if plusCount >= minusCount:
        return plus_num
    else:
        return minus_num

def remoteNum(n):
    remote = []
    n_list = list(map(int, str(n)))
    for i, num in enumerate(n_list):
        remote.append(findNum(i, num))
    return remote

def count(num):
    return len(str(num)) + plusMinus(num, n)

resNum = int(''.join(map(str, remoteNum(n))))


if m != 10:
    if count(resNum) < plusMinus(start, n):
        print(count(resNum))
    else:
        print(plusMinus(start, n))
else:
    print(plusMinus(start, n))