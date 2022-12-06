import sys          #1748번
x = str(input())
n = int(x)
total = 0
if len(x) == 1:
  print(n)
else:
  total = 9
  for i in range(1, len(x)):
    if n // (10 ** i) > 9:
      total += (((10 -1) * (10 ** i)) * (i + 1))
    else:
      total += ((n - (10 ** i  - 1)) * (i + 1))
      break
  print(total)