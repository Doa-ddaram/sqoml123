import sys
input = sys.stdin.readline
while True:
    p,q,r = map(int,input().split())
    if p+q+r == 0:
        break
    P, Q , R = p * p, q * q, r * r
    if P + Q == R or Q + R == P or P + R == Q:
        print('right')
    else:
        print('wrong')