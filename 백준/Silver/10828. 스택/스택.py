import sys 
L = []
for _ in range(int(sys.stdin.readline())):
  x = sys.stdin.readline()
  if x[0:4] == 'push':
    L.append(int(x[5:]))
  elif x[0:3] == 'pop':
    if len(L) == 0:
      print(-1)
    else:
      t = L.pop()
      print(t)
  elif x[0:4] == 'size':
    print(len(L))
  elif x[0:5] == 'empty':
    if len(L) == 0:
      print(1)
    else:
      print(0)
  elif x[0:3] == 'top':
    if len(L) == 0:
      print(-1)
    else:
      print(L[-1])