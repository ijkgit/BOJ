import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    for s in string:
        if s != '(' and s != ')'\
            and s != '[' and s != ']':
            string = string.replace(s, '')
    while '[]' in string or '()' in string:
        string = string.replace('()', '')
        string = string.replace('[]', '')
    print('no') if string else print('yes')
