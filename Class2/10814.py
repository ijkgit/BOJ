import sys
input = sys.stdin.readline

n = int(input())
user = []

for _ in range(n):
    age, name = input().split()
    user.append((age, name))

user = sorted(user, key=lambda x: int(x[0]))

for age, name in user:
    print(age, name)