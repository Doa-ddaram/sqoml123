import sys
N = int(sys.stdin.readline())
total = []
for i in range(0, N):
  L = []
  a, b, c = map(int, input().split())
  L.append(a)
  L.append(b)
  L.append(c)
  L.sort()
  if a == b == c:
    k = 10000 + L[1] * 1000
  elif a != b and b != c and c != a :
    k = L[2] * 100
  else :
    k = 1000 + L[1] * 100
  total.append(k)
total.sort()
print(total[N-1])