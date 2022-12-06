import sys
a= 1
b = 1
while True:
    a, b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0 :
        break
    print(a + b)