import sys
L = []
for _ in range(9):
  L.append(int(sys.stdin.readline()))
s = sum(L) - 100
for i in range(9):
  if L.count(s - L[i]) == 1 and L[i] != s - L[i]:
    t = L[i]
    L.remove(t)
    L.remove(s - t)
    L.sort()
    break
for j in range(7):
  print(L[j])