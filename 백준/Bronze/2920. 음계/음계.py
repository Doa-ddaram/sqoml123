asc_L = list(range(1,9))
des_L = list(range(8,0,-1))
import sys
L = list(map(int,sys.stdin.readline().split()))
if L == asc_L:
  print('ascending')
elif L == des_L:
  print('descending')
else:
  print('mixed')