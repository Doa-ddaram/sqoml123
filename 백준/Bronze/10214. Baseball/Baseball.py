import sys
for _ in range(0, int(sys.stdin.readline())):
  Yon, Ko = 0, 0
  for i in range(0, 9):
    a, b = map(int, sys.stdin.readline().split())
    Yon += a
    Ko += b
  if Yon > Ko:
    print('Yonsei')
  elif Yon < Ko:
    print('Korea')
  else:
    print('Draw')