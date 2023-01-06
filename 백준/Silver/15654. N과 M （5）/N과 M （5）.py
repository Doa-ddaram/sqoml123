import sys
N, M = map(int,input().split())
input = sys.stdin.readline
from itertools import permutations
t = list(permutations(sorted(list(map(int,input().split()))),M))
for i in range(len(t)):
  print(' '.join(map(str,t[i])))