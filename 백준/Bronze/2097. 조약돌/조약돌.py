n = int(input())
from math import sqrt
if 1 <= n <= 4:
  print(4)
elif sqrt(n) == int(sqrt(n)):
  print(4 * (int(sqrt(n))-1))
else:
  t = int(sqrt(n))
  if n > t*t + t:
    print(4 * t)
  else:
    print(4 * t - 2)