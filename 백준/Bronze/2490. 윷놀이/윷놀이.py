import sys
for _ in range(3):
    a,b,c,d = map(int,input().split())
    t = a+ b+ c+d
    if t == 1:
        print('C')
    elif t == 2:
        print('B')
    elif t == 3:
        print('A')
    elif t == 4:
        print('E')
    else:
        print('D')