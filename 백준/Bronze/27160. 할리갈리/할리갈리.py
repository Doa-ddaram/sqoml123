import sys
input = sys.stdin.readline
n = int(input())
t_L = [0 for i in range(4)]
for _ in range(n):
    temp = input().rstrip()
    if temp[0] == 'S':
        t_L[0] = t_L[0] + int(temp[-1])
    elif temp[0] == 'B':
        t_L[1] = t_L[1] + int(temp[-1])
    elif temp[0] == 'L':
        t_L[2] = t_L[2] + int(temp[-1])
    else:
        t_L[3] = t_L[3] + int(temp[-1])
if t_L[0] == 5 or t_L[1] == 5 or t_L[2] == 5 or t_L[3] == 5:
    print('YES')
else:
    print('NO')