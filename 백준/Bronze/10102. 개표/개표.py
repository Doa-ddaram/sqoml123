import sys
a = int(sys.stdin.readline())
b = list(sys.stdin.readline())
A, B = 0, 0
for i in range(0, a):
  if b[i] == 'A':
    A += 1
  else :
    B += 1
if A > B:
  print('A')
elif A < B:
  print('B')
else:
  print('Tie')