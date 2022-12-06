import sys
for _ in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    temp = 1
    if a % 10 == 0 or a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
        b = 1
    elif a % 10 == 4 or a % 10 == 9 :
        b = b % 2 + 2
    else:
        b = b % 4 + 4
    for i in range(1,b+1):
        temp *= a
        temp %= 10
    if temp:
        print(temp)
    else:
        print(10)