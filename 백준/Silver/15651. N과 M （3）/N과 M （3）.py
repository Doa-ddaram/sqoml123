import sys
input = sys.stdin.readline
N, M = map(int,input().split())
from itertools import product
t = product([str(i) for i in range(1,N+1)],repeat = M)
print('\n'.join(' '.join(temp) for temp in t))