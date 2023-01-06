import sys
from math import trunc
a,b,c = map(int,input().split())
if b >= c:
  print(-1)
else:
  print('%d' %(trunc(a / (c-b))+1))