import sys
input = sys.stdin.readline
n = int(input())
t = 1
re = 1
for _ in range(n):
    temp1,temp2 = map(str,input().split())
    temp2 = int(temp2)
    if temp1[0] == 'H':
        print(t, 'NO')
        if temp2 == t:
            t = t + re
            if t == 0:
                t = 12
            elif t == 13:
                t = 1
            continue
        else:
            re = -1 * re
    else:
        if temp2 == t:
            print(t, 'YES')
        else:
            print(t, 'NO')
    t = t + re  
    if t == 0:
        t = 12
    elif t == 13:
        t = 1