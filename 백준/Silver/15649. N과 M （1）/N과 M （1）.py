import sys
N, M = map(int,input().split())
from itertools import permutations
t = permutations([str(i) for i in range(1,N+1)],M)
print('\n'.join(' '.join(temp) for temp in t))