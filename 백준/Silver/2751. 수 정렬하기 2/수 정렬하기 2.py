import sys
L = []
for i in range(int(sys.stdin.readline())):
  L.append(int(sys.stdin.readline()))
L.sort()
for i in range(len(L)):
  print(L[i])