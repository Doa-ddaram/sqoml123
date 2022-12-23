import sys
a,b,x,y = map(int,input().split())
square_L = sorted([a,b,x-a,y-b])
print(square_L[0])

