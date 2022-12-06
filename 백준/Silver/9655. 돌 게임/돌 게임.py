import sys
n = int(sys.stdin.readline())
L = [1, 3, 5]
if L.count(n % 6) == 1:
  print('SK')
else:
  print('CY')