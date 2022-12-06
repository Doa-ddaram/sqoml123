L = []
a, b, c = map(int, input().split())
L.append(a)
L.append(b)
L.append(c)
L.sort()
if a == b == c:
  print(10000 + L[1] * 1000)
elif a != b and b != c and c != a :
  print(L[2] * 100)
else :
  print(1000 + L[1] * 100)